from django.core.management.base import BaseCommand
from Nexquality.management.commands._private import attribute_badges


class Command(BaseCommand):
    help = 'Attributes badges to all users'

    def handle(self, *args, **options):
        attribute_badges()
        self.stdout.write('Badges successfully attributed!')
