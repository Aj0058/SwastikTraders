# Generated by Django 4.2.2 on 2024-11-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0035_brands'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brands',
            old_name='image',
            new_name='Logo',
        ),
        migrations.AddField(
            model_name='brands',
            name='Description',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='brands',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
