# Generated by Django 4.0.5 on 2022-06-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_event_recurring_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurring_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]