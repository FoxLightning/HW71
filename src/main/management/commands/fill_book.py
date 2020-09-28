from django.core.management.base import BaseCommand
from main.tasks import fill_book_async


class Command(BaseCommand):
    help = 'Generate random books'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, help='Number of books to be created')

    def handle(self, *args, **kwargs):
        arg = kwargs['number']
        arg = 100 if arg is None else arg
        fill_book_async.delay(arg)
