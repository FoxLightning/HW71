from django.core.management.base import BaseCommand, CommandError
from main.utils import fill_user


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, help='Number of users to be created')

    def handle(self, *args, **kwargs):
        arg = kwargs['number']
        arg = 100 if arg is None else arg
        fill_user(number=arg)
