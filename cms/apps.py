import os
import logging
from django.apps import AppConfig
from django.conf import settings
from wagtail.core.signals import page_published, page_unpublished

from .tasks import build, develop

logger = logging.getLogger('cms')


def signal_build(sender, instance, **kwargs):
    site = instance.get_site()
    build.delay(site.id)


class CmsConfig(AppConfig):
    name = 'cms'
    label = 'cms'
    verbose_name = 'Content Management System'

    def ready(self):
        page_published.connect(
            signal_build,
            dispatch_uid='wagtailbakery_page_published'
        )

        # TODO: Fix if page.delete() to not call this signal
        # page_unpublished.connect(
        #    signal_build,
        #    dispatch_uid='wagtailbakery_page_unpublished'
        # )

        if settings.DEBUG:
            if os.environ.get('RUN_MAIN', None) != 'true':
                develop.delay()
