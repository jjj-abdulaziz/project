# Generated by Django 5.0.7 on 2024-08-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]