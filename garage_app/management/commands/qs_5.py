from django.core.management.base import BaseCommand, CommandError
from garage_app.models import CustomUser


class Command(BaseCommand):
    help = 'Вывести список менеджеров, которые задавали заказы заданному водителю'

    def add_arguments(self, parser):
        parser.add_argument('driver_id', type=int)

    def handle(self, *args, **options):
        self.stdout.write('{}'.format(CustomUser.objects.filter(order__defined_car__driver__id=options['driver_id'])))
