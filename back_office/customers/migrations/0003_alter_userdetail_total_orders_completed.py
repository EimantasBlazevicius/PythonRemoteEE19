# Generated by Django 4.2.7 on 2023-12-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_userdetails_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='total_orders_completed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
