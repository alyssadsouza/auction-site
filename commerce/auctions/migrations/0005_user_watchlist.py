# Generated by Django 3.2 on 2021-05-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.TextField(blank=True, default='', max_length=350),
        ),
    ]