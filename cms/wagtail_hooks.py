from wagtail.core import hooks
import graphene
from graphene_django.debug import DjangoDebug


class DebugQuery(object):
    debug = graphene.Field(DjangoDebug, name='_debug')


@hooks.register("register_schema_query")
def register_schema_query(query_mixins):
    query_mixins += [
        DebugQuery,
    ]
