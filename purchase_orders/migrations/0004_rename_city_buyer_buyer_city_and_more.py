# Generated by Django 5.0.1 on 2024-01-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0003_remove_orders_aceptance_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='city',
            new_name='buyer_city',
        ),
        migrations.RenameField(
            model_name='buyer',
            old_name='name',
            new_name='buyer_code',
        ),
        migrations.RenameField(
            model_name='buyer',
            old_name='region',
            new_name='buyer_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='city',
            new_name='seller_city',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='code',
            new_name='seller_code',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='name',
            new_name='seller_name',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='region',
            new_name='seller_region',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='code',
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyer_region',
            field=models.CharField(default='rm', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyer_rut',
            field=models.CharField(default='234', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyer_unit_name',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_b_specs',
            field=models.CharField(default='test', max_length=510),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_code_category',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_currency',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_net_price',
            field=models.FloatField(default='150'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_quatity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_s_specs',
            field=models.CharField(default='test', max_length=510),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_total',
            field=models.FloatField(default=156),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_total_charges',
            field=models.FloatField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_total_dscto',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_total_taxes',
            field=models.FloatField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_rut',
            field=models.CharField(default='890', max_length=20),
            preserve_default=False,
        ),
    ]