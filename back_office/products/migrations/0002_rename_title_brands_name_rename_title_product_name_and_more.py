# Generated by Django 4.2.7 on 2023-12-16 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brands',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='title',
            new_name='name',
        ),
    ]