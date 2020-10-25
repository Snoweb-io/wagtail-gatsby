import datetime
import json
import urllib

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.signing import TimestampSigner
from django.db import models
from django.shortcuts import render

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from grapple.models import (
    GraphQLStreamfield,
)

from .blocks import MyTextBlock, MyImageBlock


# https://github.com/torchbox/wagtail-torchbox/blob/master/headlesspreview/models.py

class PagePrev(models.Model):
    token = models.CharField(max_length=255, unique=True)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE, related_name="sdfsdfsdf")
    content_json = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def as_page(self):
        content = json.loads(self.content_json)
        page_model = ContentType.objects.get_for_id(content['content_type']).model_class()
        page = page_model.from_json(self.content_json)
        page.pk = content['pk']
        return page

    @classmethod
    def garbage_collect(cls):
        yesterday = datetime.datetime.now() - datetime.timedelta(hours=24)
        cls.objects.filter(created_at__lt=yesterday).delete()


class HeadlessPrev:
    @classmethod
    def get_preview_signer(cls):
        return TimestampSigner(salt='headlesspreview.token')

    def create_page_preview(self):
        if self.pk is None:
            identifier = "parent_id=%d;page_type=%s" % (self.get_parent().pk, self._meta.label)
        else:
            identifier = "id=%d" % self.pk

        return PagePrev.objects.create(
            token=self.get_preview_signer().sign(identifier),
            content_type=self.content_type,
            content_json=self.to_json(),
        )

    @classmethod
    def get_preview_url(cls, token):
        return f'{settings.PREVIEW_URL}?' + urllib.parse.urlencode({
            'content_type': cls._meta.app_label + '.' + cls.__name__.lower(),
            'token': token,
        })

    def serve_preview(self, request, mode_name):
        page_preview = self.create_page_preview()
        page_preview.save()
        PagePrev.garbage_collect()

        return render(request, 'cms/preview.html', {
            'preview_url': self.get_preview_url(page_preview.token),
        })

    @classmethod
    def get_page_from_preview_token(cls, token):
        content_type = ContentType.objects.get_for_model(cls)

        # Check token is valid
        cls.get_preview_signer().unsign(token)

        try:
            return PagePrev.objects.get(content_type=content_type, token=token).as_page()
        except PagePrev.DoesNotExist:
            return


# =================================
# TestPage used for testing purpose
# =================================


class TestPage(HeadlessPrev, Page):
    template = 'cms/preview.html'

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
