from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse


class DriversToCars(admin.TabularInline):
    model = Car.driver.through


class ManagersToOrders(admin.TabularInline):
    model = Order.manager.through


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [DriversToCars, ManagersToOrders]
    list_display = ('first_name', 'last_name', 'group')

    def group(self, obj):
        return obj.groups.first().name

    class Meta:
        app_label = 'auth'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    radio_fields = {'fuel_type': admin.VERTICAL}
    empty_value_display = ''
    inlines = [DriversToCars,]
    exclude = ('driver',)

    list_display = ('car_type', 'gos_number', 'is_ok', 'damaged_unit')
    list_display_links = ('gos_number', )

    def is_ok(self, obj):
        return not RepairTicket.objects.filter(car=obj.id).filter(is_closed=False).exists()
    
    is_ok.short_description = 'исправна'
    is_ok.boolean = True
        
    def damaged_unit(self, obj):

        ticket = RepairTicket.objects.filter(car=obj.id).filter(is_closed=False)
        if ticket:
            last_ticket = ticket.last()
            info = (RepairTicket._meta.app_label, RepairTicket._meta.model_name)
            url = reverse('admin:{}_{}_change'.format(*info), args=(last_ticket.id,))
            return format_html('<a href="{url}"> {text} </a>'.format(
                url=url, text=last_ticket.damaged_unit))
        else:
            return None
    damaged_unit.short_description = 'Узел с поломкой'


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight_capacity', 'body')

    def body(self, obj):
        return '{} x {} x {} м'.format(obj.useful_length, obj.useful_width, obj.useful_height)
    body.short_description = 'кузов'


@admin.register(RepairTicket)
class RepairTicketAdmin(admin.ModelAdmin):

    list_display = ('car', 'damaged_unit', 'is_closed', 'date_finish', 'cost')
    list_filter = ['is_closed']
    list_display_links = ('damaged_unit', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ManagersToOrders,]
    exclude = ('manager',)
    empty_value_display = '???'
    list_display = ('title', 'status_done', 'customer_data', 'defined_car')

    list_filter = ['status_done', 'defined_car']



@admin.register(PitStop)
class PitStopAdmin(admin.ModelAdmin):
    list_display = ('refuel_moment', 'car', 'fuel', 'quantity', 'price_per_liter', 'cost', 'total_mileage')
    list_filter = ['car']
    
    def fuel(self, obj):
        return obj.car.get_fuel_type_display()
    
    fuel.short_description = 'топливо'

    def cost(self, obj):
        return '{}'.format(float(obj.price_per_liter) * obj.quantity)
    
    cost.short_description = 'итого'
