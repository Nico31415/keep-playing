# Generated by Django 4.0.5 on 2022-06-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_event_coach_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='role',
            field=models.CharField(default='Coach', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='sport',
            field=models.CharField(default='Muay Thai', max_length=50),
            preserve_default=False,
        ),
    ]
