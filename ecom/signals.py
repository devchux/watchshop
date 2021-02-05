from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        first_name = instance.first_name
        last_name = instance.last_name
        fullname = f'{first_name} {last_name}'
        Customer.objects.create(customer=instance, name=fullname)