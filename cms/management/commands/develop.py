import time
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
        logger.debug("START develop")

        current_task = TaskResult.objects.filter(
            Q(task_name='cms.tasks.develop') &
            Q(status=states.STARTED)
        ).first()

        old_tasks = TaskResult.objects.all().exclude(pk=current_task.pk)
        for task in old_tasks:
            app.control.revoke(task.task_id, terminate=True, signal='SIGKILL')

        # Check if `gatsby develop` process if running
        fuser_returncode = subprocess.Popen("fuser -k 8000/tcp", shell=True).wait()
        if fuser_returncode == 0:
            # Kill `gatsby develop` process
            subprocess.Popen("fuser -k 8000/tcp", shell=True).wait()
            time.sleep(5)

        # Start fresh gatsby develop commands
        gatsby_develop_returncode = subprocess.run(
            "npm run build-plugin && gatsby clean && yes no | gatsby develop  --verbose=true",
            shell=True
        )
        if gatsby_develop_returncode != 0:
            raise DevelopError()
