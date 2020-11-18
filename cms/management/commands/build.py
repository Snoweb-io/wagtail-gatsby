import logging
import subprocess

from celery import states
from django.db.models import Q
from django.core.management.base import BaseCommand
from django_celery_results.models import TaskResult
from wagtail.core.models import Site

from cms.models import AWSSettings
from cms.exceptions import BuildIsAlreadyRunningError, BucketNameError

logger = logging.getLogger('cms')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('site_id', type=int)

    def handle(self, *args, **options):
        logger.debug("START build cms")
        logger.debug("WITH options=`%s`" % str(options))

        # 1: Manage tasks

        tasks_pending = TaskResult.objects.filter(
            Q(task_name='cms.tasks.build') &
            (Q(status=states.STARTED) | Q(status=states.RETRY))
        )

        tasks_pending_count = tasks_pending.count()
        logger.debug("WITH tasks_pending=`%d`" % tasks_pending_count)
        if tasks_pending_count > 1:
            raise BuildIsAlreadyRunningError()

        # 2: Gatsby Build

        gatsby_build = subprocess.run(["gatsby", "build"])
        logger.info("WITH `gatsby build` returncode=`%d`" % gatsby_build.returncode)

        # 3: AWS

        site_id = options['site_id']
        site = Site.objects.get(id=site_id)
        aws_settings = AWSSettings.for_site(site)
        if not aws_settings.bucket:
            raise BucketNameError()
        aws_settings.s3_deploy()
        aws_settings.cloud_front_invalidation()
        logger.debug(aws_settings.preview_url)
        logger.debug("END build cms")
