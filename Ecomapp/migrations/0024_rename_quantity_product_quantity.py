# Generated by Django 4.2.2 on 2024-08-06 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0023_product_description2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
