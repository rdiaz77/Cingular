# Generated by Django 5.0.1 on 2024-01-06 03:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]