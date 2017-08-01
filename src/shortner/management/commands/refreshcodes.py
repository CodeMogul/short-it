from django.core.management.base import BaseCommand, CommandError

from shortner.models import ShortItURL

class Command(BaseCommand):
    '''
        Custom Command refreshcode

        Refresh shortcodes using "python manage.py refreshcodes"
    '''
    help = 'Refreshes short codes for all urls in the database'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return ShortItURL.objects.refresh_shortcodes(items=options['items'])