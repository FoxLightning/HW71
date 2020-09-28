from django.core.management.base import BaseCommand
from main.utils import fill_category


class Command(BaseCommand):
    help = 'Fill categories random words'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, help='Number of categories to be created')

    def handle(self, *args, **kwargs):
        arg = kwargs['number']
        arg = 10 if arg is None else arg
        fill_category(number=arg)

