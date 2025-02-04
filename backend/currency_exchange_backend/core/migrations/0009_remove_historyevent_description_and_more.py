# Generated by Django 5.1.4 on 2025-01-04 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_historyevent_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historyevent',
            name='description',
        ),
        migrations.AddField(
            model_name='historyevent',
            name='target_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='targeted_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historyevent',
            name='event_type',
            field=models.CharField(choices=[('create_user', 'Create User'), ('delete_user', 'Delete User'), ('update_user', 'Update User'), ('create_currency', 'Create Currency'), ('delete_currency', 'Delete Currency'), ('update_currency', 'Update Currency')], max_length=20),
        ),
        migrations.AlterField(
            model_name='historyevent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performed_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
