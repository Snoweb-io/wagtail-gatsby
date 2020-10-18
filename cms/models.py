from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from grapple.models import (
    GraphQLString,
    GraphQLStreamfield,
)

from .blocks import TextBlock, ImageBlock


# =================================
# TestPage used for testing purpose
# =================================


class TestPage(Page):
    body = StreamField([
        ('text', TextBlock()),
        ('image', ImageBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    graphql_fields = [
        GraphQLStreamfield("body"),
    ]
