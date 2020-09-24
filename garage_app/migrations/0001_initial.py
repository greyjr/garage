# Generated by Django 2.2 on 2020-09-17 18:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gos_number', models.CharField(max_length=16, unique=True, verbose_name='госномер')),
                ('fuel_consumption', models.FloatField(verbose_name='расход топлива')),
            ],
            options={
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='модель')),
                ('weight_capacity', models.FloatField(verbose_name='грузоподъемность')),
                ('useful_lenght', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='длина')),
                ('useful_width', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='ширина')),
                ('useful_height', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='высота')),
            ],
            options={
                'verbose_name_plural': 'Модели машин',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='вид топлива')),
            ],
            options={
                'verbose_name_plural': 'Виды топлива',
            },
        ),
        migrations.CreateModel(
            name='RepairTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='начало ремонта')),
                ('date_finish', models.DateTimeField(blank=True, null=True, verbose_name='выход из ремонта')),
                ('damaged_unit', models.CharField(max_length=32, verbose_name='неисправный узел/агрегат')),
                ('damage_description', models.TextField(max_length=512, verbose_name='подробное описание поломки')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='стоимость ремонта')),
                ('is_closed', models.BooleanField(default=False, verbose_name='статус ремонта')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garage_app.Car', verbose_name='машина')),
            ],
            options={
                'verbose_name_plural': 'Ремонтные листы',
            },
        ),
        migrations.CreateModel(
            name='PitStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refuel_moment', models.DateTimeField(verbose_name='дата/время заправки')),
                ('quantity', models.FloatField(verbose_name='литров')),
                ('price_per_liter', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='цена за литр')),
                ('total_mileage', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='полный пробег')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garage_app.Car', verbose_name='машина')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='шкаф', max_length=32, verbose_name='наименование заказа')),
                ('weight', models.FloatField(verbose_name='масса груза')),
                ('height', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='максимальная высота груза')),
                ('lenght', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='максимальная длина груза')),
                ('width', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='максимальная ширина груза')),
                ('customer_data', models.CharField(max_length=128, verbose_name='фамилия, адрес, телефон клиента')),
                ('registration_date', models.DateField(verbose_name='дата формирования заказа')),
                ('status_done', models.BooleanField(default=False, verbose_name='выполнено')),
                ('defined_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defined_cars', related_query_name='defined_car', to='garage_app.Car')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage_app.CarType', to_field='name'),
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'drivers'}, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garage_app.Fuel'),
        ),
    ]
