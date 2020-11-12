from django.core.management.base import BaseCommand
from grapple.schema import schema


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(schema)
