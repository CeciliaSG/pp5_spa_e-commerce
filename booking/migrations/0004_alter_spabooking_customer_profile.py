# Generated by Django 4.2.13 on 2024-06-05 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('booking', '0003_spabookingservices_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spabooking',
            name='customer_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SpaBookings', to='accounts.customerprofile'),
        ),
    ]
