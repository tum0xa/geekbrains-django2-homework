# Generated by Django 2.1 on 2019-01-30 17:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='customer',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 17, 0, 54, 651801, tzinfo=utc)),
        ),
    ]
