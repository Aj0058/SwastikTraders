# Generated by Django 4.2.2 on 2024-07-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0012_alter_arrival_mrp_alter_arrival_sp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='path/to/upload')),
            ],
        ),
    ]