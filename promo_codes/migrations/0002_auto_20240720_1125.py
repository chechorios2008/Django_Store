# Generated by Django 2.2.3 on 2024-07-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo_codes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='valid_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='valid_to',
            field=models.DateTimeField(),
        ),
    ]
