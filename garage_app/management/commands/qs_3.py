from django.core.management.base import BaseCommand, CommandError
from garage_app.models import CustomUser


class Command(BaseCommand):
    help = 'Вывести список водителей, машины которых в данный момент ремонтируются'

    def handle(self, *args, **options):
        self.stdout.write('{}'.format(list(CustomUser.objects.filter(car__repair_ticket__is_closed=False))))

