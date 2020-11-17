import logging
from django.apps import AppConfig
from django.conf import settings
from wagtail.core.signals import page_published, page_unpublished

from .tasks import build, develop

logger = logging.getLogger('cms')


def signal_build(**kwargs):
    build.delay()


class CmsConfig(AppConfig):
    name = 'cms'
    label = 'cms'
    verbose_name = 'Content Management System'

    def ready(self):
        page_published.connect(
            signal_build,
            dispatch_uid='wagtailbakery_page_published'
        )
        page_unpublished.connect(
            signal_build,
            dispatch_uid='wagtailbakery_page_unpublished'
        )
        if settings.DEBUG:
            develop.delay()
