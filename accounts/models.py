from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomerProfile(models.Model):
    """
    From Boutique Ado Walkthrough.
    """
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.customer.username
        

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(customer=instance)
    instance.customerprofile.save()