# Generated by Django 4.2.2 on 2024-07-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0019_rename_email_feedback_email2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Product2',
            field=models.CharField(max_length=200),
        ),
    ]
