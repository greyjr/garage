from django.core.management.base import BaseCommand, CommandError
from garage_app.models import CustomUser


class Command(BaseCommand):
    help = 'Вывести список водителей, которые ездили на заданной машине'

    def add_arguments(self, parser):
        parser.add_argument('car_id', type=int)

    def handle(self, *args, **options):
        self.stdout.write('{}'.format(CustomUser.objects.filter(car__id=options['car_id'])))
