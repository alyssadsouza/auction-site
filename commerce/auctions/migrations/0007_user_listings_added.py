# Generated by Django 3.2 on 2021-05-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210504_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='listings_added',
            field=models.ManyToManyField(blank=True, related_name='publisher', to='auctions.Listing'),
        ),
    ]
