# Generated by Django 5.0.1 on 2024-07-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shiftbooking', '0002_geofencing_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geofencing',
            old_name='latitute',
            new_name='cordinates',
        ),
        migrations.RemoveField(
            model_name='geofencing',
            name='longitute',
        ),
    ]
