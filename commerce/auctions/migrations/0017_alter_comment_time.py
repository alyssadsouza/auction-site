# Generated by Django 3.2 on 2021-05-05 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 5, 14, 46, 35, 728665, tzinfo=utc)),
        ),
    ]