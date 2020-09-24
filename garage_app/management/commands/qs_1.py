from django.core.management.base import BaseCommand, CommandError
from garage_app.models import Order


class Command(BaseCommand):
    help = 'Вывести список будущих задач на доставку для заданного водителя'

    def add_arguments(self, parser):
        parser.add_argument('driver_id', type=int)

    def handle(self, *args, **options):
        orders = Order.objects.filter(defined_car__driver__id=options['driver_id']).filter(status_done=False) or 'нет заказов'
        self.stdout.write(self.style.WARNING('Предстоящие заказы: {}'.format(orders)))