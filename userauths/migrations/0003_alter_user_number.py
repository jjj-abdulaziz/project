# Generated by Django 5.0.7 on 2024-07-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
