import logging
import subprocess
from django.db.models import Q
from django.core.management.base import BaseCommand
from django_celery_results.models import TaskResult
from celery import states

from cms.exceptions import BuildIsAlreadyRunningError

logger = logging.getLogger('cms')


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug("Start build cms")

        tasks_pending = TaskResult.objects.filter(
            Q(task_name='cms.tasks.build') &
            Q(status=states.STARTED) |
            Q(status=states.RETRY)
        )

        tasks_pending_count = tasks_pending.count()
        logger.debug("WITH tasks_pending=`%d`" % tasks_pending_count)

        if tasks_pending_count > 1:
            raise BuildIsAlreadyRunningError()

        gatsby_build = subprocess.run(["gatsby", "build"])
        logger.info("WITH returncode=`%d`" % gatsby_build.returncode)

        logger.debug("End build cms")
