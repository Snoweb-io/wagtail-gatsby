import logging
from django.conf import settings
from django.shortcuts import redirect
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from grapple.models import (
    GraphQLStreamfield,
)

from .blocks import MyTextBlock, MyImageBlock


class HeadlessMixin(object):
    def get_client_root_url(self):
        try:
            return settings.HEADLESS_PREVIEW_CLIENT_URLS[self.get_site().hostname]
        except (AttributeError, KeyError):
            return settings.HEADLESS_PREVIEW_CLIENT_URLS["default"]

    def get_preview_url(self):
        return "%s%s?preview=1" % (
            self.get_client_root_url(),
            self.slug
        )

    def serve_preview(self, request, mode_name):
        return redirect(self.get_preview_url())


class TestPage(HeadlessMixin, Page):
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
