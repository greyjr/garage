# Generated by Django 2.2 on 2020-09-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0007_auto_20200921_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairticket',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repair_tickets', related_query_name='repair_ticket', to='garage_app.Car', verbose_name='машина'),
        ),
    ]
