# Generated by Django 4.0.5 on 2022-08-22 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0024_post_data_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data_time',
        ),
        migrations.AddField(
            model_name='post',
            name='data_times',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 17, 13, 52, 794408, tzinfo=utc)),
        ),
    ]
