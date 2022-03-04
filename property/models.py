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
    increase_price_per_person = models.IntegerField()
    available = models.BooleanField(default=True)
    complementary_breakfast = models.BooleanField(default=False)
    luxirous_room = models.BooleanField(default=False)
    attached_bathroom = models.BooleanField(default=False)
    hot_shower = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    smoking_drinking = models.BooleanField(default=False)
    receive_facility = models.BooleanField(default=False)
    drop_facility = models.BooleanField(default=False)
    city =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nearest_landmark = models.CharField(max_length=255)
    rules = models.TextField()
    main_image = models.ImageField(upload_to= "property/main_image")


class PropertyImages(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'property/other_images')


