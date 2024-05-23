# Generated by Django 4.2.13 on 2024-05-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_spaservice_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaservice',
            name='available_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spaservice',
            name='available_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
