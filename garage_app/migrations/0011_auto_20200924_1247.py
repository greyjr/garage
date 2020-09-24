# Generated by Django 2.2 on 2020-09-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_app', '0010_auto_20200921_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_done',
            field=models.BooleanField(db_index=True, default=False, verbose_name='выполнено'),
        ),
        migrations.AlterField(
            model_name='repairticket',
            name='is_closed',
            field=models.BooleanField(db_index=True, default=False, verbose_name='статус ремонта'),
        ),
    ]