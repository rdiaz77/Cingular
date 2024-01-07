# Generated by Django 5.0.1 on 2024-01-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0005_remove_product_product_code_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_currency',
        ),
        migrations.AddField(
            model_name='product',
            name='product_code_category',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]