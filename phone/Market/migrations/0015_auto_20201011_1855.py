# Generated by Django 2.2.10 on 2020-10-11 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0014_auto_20201011_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 15, 55, 9, 983567, tzinfo=utc)),
        ),
    ]
