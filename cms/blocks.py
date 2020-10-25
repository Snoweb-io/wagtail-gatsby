import requests
from io import BytesIO
from django.core.files.images import ImageFile
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.images.models import Image
from grapple.helpers import register_streamfield_block
from grapple.models import (
    GraphQLString,
    GraphQLImage
)
from . import constants


# ===============================
# Blocks used for testing purpose
# ===============================

@register_streamfield_block
class MyTextBlock(blocks.StructBlock):
    text = blocks.TextBlock()

    @staticmethod
    def mock(content):
        return {
            'type': 'text',
            'value': {
                'text': str.strip(content)
            }
        }

    graphql_fields = [
        GraphQLString("text"),
    ]


@register_streamfield_block
class MyImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    @staticmethod
    def mock(title):
        url = str.strip(constants.URL_IMAGE_MOCK_1)
        filename = "%s.png" % title
        try:
            ret = Image.objects.get(title=title)
        except Image.DoesNotExist:
            response = requests.get(url)
            file = ImageFile(BytesIO(response.content), name=filename)
            ret = Image(
                title=title,
                file=file
            )
            ret.save()
        return {
            'type': 'image',
            'value': {
                'image': ret.id
            }
        }

    graphql_fields = [
        GraphQLImage("image"),
    ]
