# Generated by Django 5.0.7 on 2024-08-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.JSONField(default=dict),
        ),
    ]
