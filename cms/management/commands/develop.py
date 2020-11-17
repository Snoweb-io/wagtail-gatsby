import subprocess
import logging
from django.db.models import Q
from django.core.management.base import BaseCommand
from django_celery_results.models import TaskResult
from celery import states

from cms.tasks import app
from cms.exceptions import DevelopError

logger = logging.getLogger('cms')


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.debug("Start gatsby develop")

        current_task = TaskResult.objects.filter(
            Q(task_name='cms.tasks.develop') &
            Q(status=states.STARTED)
        ).first()

        # TODO: find a way to terminate gatsby develop

        subprocess.run(
            "npm run build-plugin && gatsby clean && yes no | gatsby develop  --verbose=true",
            shell=True
        )
        app.control.revoke(current_task.task_id, terminate=True, signal='SIGKILL')

        raise DevelopError()
