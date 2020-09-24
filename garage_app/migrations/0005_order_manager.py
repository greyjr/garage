# Generated by Django 2.2 on 2020-09-21 13:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0004_auto_20200918_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manager',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'managers'}, related_name='managers', related_query_name='manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
