# Generated by Django 4.2.2 on 2024-11-20 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0039_ordertracker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='Productimg',
        ),
    ]