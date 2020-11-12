from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail_headless_preview.models import HeadlessPreviewMixin
from grapple.models import (
    GraphQLStreamfield,
)

from .blocks import MyTextBlock, MyImageBlock


class TestPage(HeadlessPreviewMixin, Page):
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
