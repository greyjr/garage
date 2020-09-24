from django.core.management.base import BaseCommand, CommandError
from garage_app.models import Car


class Command(BaseCommand):
    help = 'Вывести список машин, которые могут выполнить заказ по перевозке груза массой 400 кг и габаритами 3x2x1м на заданное число в ближайшем будущем отсортированные по грузоподъемности'

    def add_arguments(self, parser):
        parser.add_argument('length', type=float)
        parser.add_argument('width', type=float)
        parser.add_argument('height', type=float)
        parser.add_argument('weight', type=float)

    def handle(self, *args, **options):
        cargo_data = sorted([options['length'], options['width'], options['height']]) + [options['weight']]
        working_ordered_cars = list(Car.objects.select_related('car_type').exclude(repair_ticket__is_closed=False).order_by('car_type__weight_capacity'))
        for car in working_ordered_cars[:]:
            car_data = sorted([car.car_type.useful_length, car.car_type.useful_width, car.car_type.useful_height]) + [car.car_type.weight_capacity]
            if not all(map(lambda a, b: a >= b, car_data, cargo_data)):
                working_ordered_cars.remove(car)
        self.stdout.write('{}'.format(working_ordered_cars))

