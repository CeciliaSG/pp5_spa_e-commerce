# Generated by Django 4.2.13 on 2024-05-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_remove_spaservice_available_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='availability',
            name='date',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='start_time',
        ),
        migrations.AddField(
            model_name='availability',
            name='specific_dates',
            field=models.ManyToManyField(to='services.specificdate'),
        ),
        migrations.AddField(
            model_name='availability',
            name='time_slots',
            field=models.ManyToManyField(to='services.timeslot'),
        ),
    ]
