from django.db.models.signals import post_delete, pre_delete, pre_save
from django.dispatch import receiver
from .models import SpecificDate, Availability, TimeSlotAvailability, TimeSlot
from booking.models import SpaBooking, SpaBookingServices


@receiver(pre_delete, sender=SpaBookingServices)
def pre_delete_spa_booking_service(sender, instance, **kwargs):
    """
    Signal to update the associated time slots' availability when a service is deleted or canceled.
    """
    selected_date = instance.date_and_time.date()

    try:
        time_slot = TimeSlot.objects.get(spa_service=instance.spa_service, time=instance.date_and_time.time())
    except TimeSlot.DoesNotExist:
        return

    try:
        specific_date = SpecificDate.objects.get(date=selected_date)
        TimeSlotAvailability.objects.filter(
            specific_date=specific_date,
            time_slot=time_slot,
            availability__spa_service=instance.spa_service
        ).update(is_available=True, is_booked=False)
    except (SpecificDate.DoesNotExist, Availability.DoesNotExist):
        pass


@receiver(pre_save, sender=SpaBookingServices)
def pre_save_spa_booking_service(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = SpaBookingServices.objects.get(pk=instance.pk)
            
            if old_instance.date_and_time != instance.date_and_time:
                old_selected_date = old_instance.date_and_time.date()
                try:
                    old_time_slot = TimeSlot.objects.get(
                        spa_service=old_instance.spa_service,
                        time=old_instance.date_and_time.time()
                    )
                    old_specific_date = SpecificDate.objects.get(date=old_selected_date)
                    TimeSlotAvailability.objects.filter(
                        specific_date=old_specific_date,
                        time_slot=old_time_slot,
                        availability__spa_service=old_instance.spa_service
                    ).update(is_available=True, is_booked=False)
                except (SpecificDate.DoesNotExist, TimeSlot.DoesNotExist, Availability.DoesNotExist):
                    pass

                new_selected_date = instance.date_and_time.date()
                try:
                    new_time_slot = TimeSlot.objects.get(
                        spa_service=instance.spa_service,
                        time=instance.date_and_time.time()
                    )
                    new_specific_date = SpecificDate.objects.get(date=new_selected_date)
                    TimeSlotAvailability.objects.filter(
                        specific_date=new_specific_date,
                        time_slot=new_time_slot,
                        availability__spa_service=instance.spa_service
                    ).update(is_available=False, is_booked=True)
                except (SpecificDate.DoesNotExist, TimeSlot.DoesNotExist, Availability.DoesNotExist):
                    pass

        except SpaBookingServices.DoesNotExist:
            pass









