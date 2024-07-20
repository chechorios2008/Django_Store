# Generated by Django 2.2.3 on 2024-07-19 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
        ('orders', '0002_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_addresses.ShippingAddress'),
        ),
    ]
