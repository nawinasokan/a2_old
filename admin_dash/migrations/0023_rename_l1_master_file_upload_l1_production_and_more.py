# Generated by Django 5.1.4 on 2025-01-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0022_file_upload_l1_picked_by_file_upload_l2_picked_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file_upload',
            old_name='l1_master',
            new_name='l1_production',
        ),
        migrations.RenameField(
            model_name='file_upload',
            old_name='l2_master',
            new_name='l2_production',
        ),
        migrations.RenameField(
            model_name='file_upload',
            old_name='l3_master',
            new_name='l3_production',
        ),
    ]
