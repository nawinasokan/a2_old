# Generated by Django 5.1.4 on 2025-01-22 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0009_asindata_picked_by'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role',
            unique_together={('user', 'role_type')},
        ),
    ]
