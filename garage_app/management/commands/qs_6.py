from django.core.management.base import BaseCommand, CommandError
from garage_app.models import CustomUser


class Command(BaseCommand):
    help = 'Вывести список водителей, которые обслуживали заказы заданного менеджера отсортированные по общему пробегу'
    # по пробегу сортируются машины. Поскольку машины с водителями М2М, сортировка водителей через машины вернет шум, а не информацию

    def add_arguments(self, parser):
        parser.add_argument('manager_id', type=int)

    def handle(self, *args, **options):
        self.stdout.write('{}'.format(CustomUser.objects.filter(car__order__manager__id=options['manager_id'])))
