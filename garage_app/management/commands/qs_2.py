from django.core.management.base import BaseCommand, CommandError
from garage_app.models import PitStop
from django.utils import timezone


class Command(BaseCommand):
    help = 'Вывести информацию по всем заправкам конкретного водителя за последние 30 дней (вид топлива, количество топлива, цена)'

    def add_arguments(self, parser):
        parser.add_argument('driver_id', type=int)

    def handle(self, *args, **options):
        refuel_time_range = {
            'refuel_moment__gte': timezone.now() - timezone.timedelta(days=30),
            'refuel_moment__lte': timezone.now()
        }
        pitstops = PitStop.objects.select_related('car').filter(car__driver__id=options['driver_id']).filter(**refuel_time_range)

        for one in pitstops:
            self.stdout.write('{} {} {} {}'.format(one.refuel_moment, one.car.get_fuel_type_display(), one.quantity, one.price_per_liter), ending='\n')


