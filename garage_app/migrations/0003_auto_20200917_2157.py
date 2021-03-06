# Generated by Django 2.2 on 2020-09-17 21:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0002_auto_20200917_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'drivers'}, related_name='drivers', related_query_name='driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
