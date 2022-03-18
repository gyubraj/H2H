from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from contact.email import send_contact_email

# Create your models here.

class Contact(models.Model):

    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=100)
    query = models.TextField()
    subject= models.CharField(max_length=255)



@receiver(post_save, sender=Contact)
def send_activation_email(sender, instance, created, **kwargs):

    if created:
        send_contact_email(instance)
