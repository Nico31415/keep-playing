# Generated by Django 4.0.5 on 2022-06-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_remove_organiser_default_location_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='default_location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='organiser',
            name='default_role',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='organiser',
            name='default_sport',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]