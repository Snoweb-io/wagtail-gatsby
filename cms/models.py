import time
import boto3
import logging
import os
import magic
from django.db import models
from django.conf import settings
from wagtail.contrib.settings.models import register_setting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.models import ClusterableModel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Site
from wagtail.admin.edit_handlers import StreamFieldPanel
from grapple.models import (
    GraphQLStreamfield, GraphQLString
)

from .blocks import MyTextBlock, MyImageBlock
from .mixins import HeadlessPageMixin, HeadlessSettingMixin

logger = logging.getLogger('cms')


# Pages

class TestPage(HeadlessPageMixin, Page):
    body = StreamField([
        ('text', MyTextBlock()),
        ('image', MyImageBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    graphql_fields = [
        GraphQLStreamfield("body"),
    ]


# Settings


@register_setting
class ThemeSettings(HeadlessSettingMixin, ClusterableModel):
    primary = models.CharField(default='', blank=True, max_length=10)
    secondary = models.CharField(default='', blank=True, max_length=10)

    colors_panel = [
        FieldPanel('primary'),
        FieldPanel('secondary'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(colors_panel, heading='Colors'),
    ])

    graphql_fields = [
        GraphQLString("primary"),
        GraphQLString("secondary"),
    ]

    class Meta:
        verbose_name = 'Theme'


@register_setting
class AWSSettings(HeadlessSettingMixin, ClusterableModel):
    client_s3 = boto3.client('s3')
    client_cloud_front = boto3.client('cloudfront')
    public_directory = "./public"
    destination = ""

    bucket = models.CharField(default='', blank=True, max_length=100)

    class Meta:
        verbose_name = 'AWS'

    deployment_panel = [
        FieldPanel('bucket'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(deployment_panel, heading='Deployment'),
    ])

    @property
    def preview_url(self):
        bucket = self.client_s3.get_bucket_location(Bucket=self.bucket)
        return "http://%s.s3-website.%s.amazonaws.com" % (
            self.bucket,
            bucket['LocationConstraint'],
        )

    def s3_deploy(self):
        response = self.client_s3.list_buckets()
        logger.debug("List Buckets for occurence `%s`" % self.bucket)
        bucket_is_created = False
        for bucket in response['Buckets']:
            logger.debug("Bucket `%s`" % bucket["Name"])
            if bucket["Name"] == self.bucket:
                bucket_is_created = True

        if not bucket_is_created:
            location = {'LocationConstraint': settings.AWS_S3_REGION_NAME}
            self.client_s3.create_bucket(
                Bucket=self.bucket,
                CreateBucketConfiguration=location
            )
            self.client_s3.put_bucket_website(
                Bucket=self.bucket,
                WebsiteConfiguration={
                    'ErrorDocument': {'Key': 'error.html'},
                    'IndexDocument': {'Suffix': 'index.html'},
                }
            )

        for root, dirs, files in os.walk(self.public_directory):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, self.public_directory)
                s3_path = os.path.join(self.destination, relative_path)
                content_type = magic.from_file(local_path, mime=True)

                logger.debug('Uploading `%s` with content_type `%s` in `%s`' % (
                    s3_path,
                    content_type,
                    self.bucket,
                ))
                self.client_s3.upload_file(
                    local_path,
                    self.bucket,
                    s3_path,
                    ExtraArgs={'Metadata': settings.AWS_S3_OBJECT_PARAMETERS}
                )
                self.client_s3.put_object(
                    Bucket=self.bucket,
                    Key=s3_path,
                    Body=open(local_path, 'rb'),
                    ContentType=content_type,
                    ContentDisposition='inline',
                )
                self.client_s3.put_object_acl(
                    ACL='public-read',
                    Bucket=self.bucket,
                    Key=s3_path
                )

    def cloud_front_invalidation(self):
        if settings.AWS_DISTRIBUTION_ID:
            response = self.client_cloud_front.create_invalidation(
                DistributionId=settings.AWS_DISTRIBUTION_ID,
                InvalidationBatch={
                    'Paths': {
                        'Quantity': 1,
                        'Items': [
                            '/*'
                        ],
                    },
                    'CallerReference': str(time.time()).replace(".", "")
                }
            )
            logger.debug("Invalidation response: `%s`" % str(response))
