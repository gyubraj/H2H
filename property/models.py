from django.db import models
from user.models import User

# Create your models here.

property_type = (
    ('Homestay','Homestay'),
    ('Villa','Villa'),
    ('Hotel','Hotel')
)

class Property(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=40, choices=property_type)
    name = models.CharField(max_length=255)
    total_rooms = models.IntegerField()
    price_per_room = models.IntegerField()
    person_per_room = models.IntegerField()
    available = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to= "property/main_image")


class PropertyImages(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'property/other_images')


