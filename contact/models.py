from django.db import models

# Create your models here.

class Contact(models.model):

    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=100)
    query = models.TextField()

    
