# Generated by Django 4.2.2 on 2024-07-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0014_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]