# Generated by Django 4.2.13 on 2024-07-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_timeslot_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaservice',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=0),
        ),
    ]
