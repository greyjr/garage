# Generated by Django 2.2 on 2020-09-21 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0008_auto_20200921_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'drivers'}, related_name='cars', related_query_name='car', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='defined_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', related_query_name='order', to='garage_app.Car'),
        ),
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'managers'}, related_name='orders', related_query_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]
