# Generated by Django 4.0.5 on 2022-06-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_coach_experience_coach_flexibility_coach_reliability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]
