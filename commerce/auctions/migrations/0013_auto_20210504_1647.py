# Generated by Django 3.2 on 2021-05-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20210504_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('FSH', 'Fashion'), ('TOY', 'Toys'), ('ETC', 'Electronics'), ('HOM', 'Home')], max_length=3),
        ),
    ]