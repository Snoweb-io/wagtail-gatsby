import logging
from graphene_django.debug.middleware import DjangoDebugMiddleware

logger = logging.getLogger('cms')


class LoggingGQL(DjangoDebugMiddleware):
    def resolve(self, next, root, info, **args):
        promise = super().resolve(next, root, info, **args)
        logger.debug(promise)
        return promise
