from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class CarType(models.Model):
    name = models.CharField('модель', max_length=32, unique=True)
    weight_capacity = models.FloatField('грузоподъемность')
    useful_length = models.DecimalField('длина', max_digits=3, decimal_places=1)
    useful_width = models.DecimalField('ширина', max_digits=3, decimal_places=1)
    useful_height = models.DecimalField('высота', max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Модели машин"


class Car(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, to_field='name')
    gos_number = models.CharField('госномер', max_length=16, unique=True)
    FUEL_TYPES = (
        ('p', 'petrol'),
        ('d', 'diesel'),
        ('g', 'gas'),
    )
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPES, default='p')
    fuel_consumption = models.FloatField('расход топлива')

    driver = models.ManyToManyField(settings.AUTH_USER_MODEL, limit_choices_to={
        'groups__name': settings.DRIVERS_GROUP}, related_name='cars', related_query_name='car')

    def __str__(self):
        return '{}, {}'.format(self.car_type, self.gos_number)

    class Meta:
        verbose_name_plural = 'Машины'


class PitStop(models.Model):
    """
    регистрация заправки/пробега
    """
    refuel_moment = models.DateTimeField('дата/время заправки')
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, related_query_name='pitstop', 
        related_name='pitstops', null=True, verbose_name='машина')
    quantity = models.FloatField('литров')
    price_per_liter = models.DecimalField('цена за литр', decimal_places=2, max_digits=6)
    total_mileage = models.DecimalField('полный пробег', decimal_places=1, max_digits=10)

    def __str__(self):
        return '{} ({} - {}) {}л, {}грн/л'.format(self.refuel_moment.date(), self.car, 
        self.car.fuel_type, self.quantity, self.price_per_liter)

    class Meta:
        verbose_name_plural = 'заправки'


class RepairTicket(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True,
        related_name='repair_tickets', related_query_name='repair_ticket', verbose_name='машина')
    date_start = models.DateTimeField('начало ремонта')
    date_finish = models.DateTimeField('выход из ремонта', blank=True, null=True)
    damaged_unit = models.CharField('неисправный узел/агрегат', max_length=32)
    damage_description = models.TextField('подробное описание поломки', max_length=512)
    cost = models.DecimalField('стоимость ремонта', decimal_places=2, max_digits=8)
    is_closed = models.BooleanField('ремонт окончен', default=False, db_index=True)

    def __str__(self):
        return '{} - {}'.format(self.damaged_unit, self.car)

    class Meta:
        verbose_name_plural = "Ремонтные листы"


class Order(models.Model):
    """
    карточка резервирования заказа: 
     - вес/объем груза
     - инфо про заказчика
     - статус выполнения 
     - назначенный автомобиль (если пусто - еще не назначен)
    """
    title = models.CharField('наименование заказа', max_length=32, blank=True, default='шкаф')
    weight = models.FloatField('масса груза')
    height = models.DecimalField('максимальная высота груза', max_digits=3, decimal_places=1)
    length = models.DecimalField('максимальная длина груза', max_digits=3, decimal_places=1)
    width = models.DecimalField('максимальная ширина груза', max_digits=3, decimal_places=1)
    customer_data = models.CharField('фамилия, адрес, телефон клиента', max_length=128)
    registration_date = models.DateField('дата формирования заказа')
    status_done = models.BooleanField('выполнено', default=False, db_index=True)

    manager = models.ManyToManyField(settings.AUTH_USER_MODEL, limit_choices_to={
        'groups__name': settings.MANAGERS_GROUP}, related_name='orders', related_query_name='order')


    defined_car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, 
    related_name='orders', related_query_name='order', blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.customer_data)

    class Meta:
        verbose_name_plural = 'Заказы'
