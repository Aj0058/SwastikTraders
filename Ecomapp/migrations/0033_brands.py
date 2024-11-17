# Generated by Django 4.2.2 on 2024-11-15 06:55

import Ecomapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0032_delete_vidio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Ecomapp.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]