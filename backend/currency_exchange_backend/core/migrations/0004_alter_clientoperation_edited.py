# Generated by Django 5.1.4 on 2024-12-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_clientoperation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientoperation',
            name='edited',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
