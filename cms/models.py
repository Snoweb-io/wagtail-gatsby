from django.db import models
from wagtail.contrib.settings.models import register_setting
from wagtail.contrib.settings.models import BaseSetting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.models import ClusterableModel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Site
from wagtail.admin.edit_handlers import StreamFieldPanel
from grapple.models import (
    GraphQLStreamfield, GraphQLString
)

from .blocks import MyTextBlock, MyImageBlock
from .mixins import HeadlessMixin


# Pages

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


# Settings


@register_setting
class ThemeSettings(BaseSetting, ClusterableModel):
    primary = models.CharField(default='', blank=True, max_length=10)
    secondary = models.CharField(default='', blank=True, max_length=10)

    colors_panel = [
        FieldPanel('primary'),
        FieldPanel('secondary'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(colors_panel, heading='Colors'),
    ])

    graphql_fields = [
        GraphQLString("primary"),
        GraphQLString("secondary"),
    ]

    class Meta:
        verbose_name = 'Theme'
