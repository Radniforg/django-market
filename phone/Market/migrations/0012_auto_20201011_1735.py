# Generated by Django 2.2.10 on 2020-10-11 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0011_auto_20201011_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 14, 35, 36, 153296, tzinfo=utc)),
        ),
    ]