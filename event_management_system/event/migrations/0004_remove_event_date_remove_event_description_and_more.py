# Generated by Django 4.2.3 on 2024-01-04 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_attendee_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.DeleteModel(
            name='Attendee',
        ),
    ]
