# Generated by Django 2.2 on 2020-09-21 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0009_auto_20200921_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitstop',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pitstops', related_query_name='pitstop', to='garage_app.Car', verbose_name='машина'),
        ),
    ]