# Generated by Django 4.2.2 on 2024-11-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0038_orderhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=10)),
                ('Total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Status', models.CharField(default='Pending', max_length=50)),
                ('tracking_no', models.CharField(max_length=50, unique=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]