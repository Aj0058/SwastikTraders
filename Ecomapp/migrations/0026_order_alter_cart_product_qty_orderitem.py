# Generated by Django 4.2.2 on 2024-08-12 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecomapp', '0025_alter_cart_product_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=150)),
                ('Lname', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Phone', models.CharField(max_length=150)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Country', models.CharField(max_length=150)),
                ('Pincode', models.CharField(max_length=150)),
                ('Total_price', models.FloatField(max_length=150)),
                ('Payment_mode', models.CharField(max_length=150)),
                ('Payment_Id', models.CharField(max_length=250)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Out of Shipping', 'Out of Shipping'), ('Completed', 'Completed')], default='Pending', max_length=190)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.TextField(max_length=150, null=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.order')),
            ],
        ),
    ]