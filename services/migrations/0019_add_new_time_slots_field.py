# Generated by Django 4.2.13 on 2024-07-29 12:21

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_remove_old_time_slots_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='new_time_slots',
            field=models.ManyToManyField(to='services.TimeSlot', through='services.TimeSlotAvailability'),
        ),
    ]
