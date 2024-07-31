# Generated by Django 4.2.13 on 2024-07-29 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_merge_20240729_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='is_available',
        ),
        migrations.CreateModel(
            name='TimeSlotAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.availability')),
                ('specific_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.specificdate')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.timeslot')),
            ],
            options={
                'unique_together': {('availability', 'specific_date', 'time_slot')},
            },
        ),
        migrations.AddField(
            model_name='availability',
            name='time_slots',
            field=models.ManyToManyField(through='services.TimeSlotAvailability', to='services.timeslot'),
        ),
    ]
