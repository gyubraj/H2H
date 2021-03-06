from django.db import models
from django.db.models import Q

import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from user.models import User
from property.email import send_property_added_email

# Create your models here.

property_type = (
    ('Homestay','Homestay'),
    ('Villa','Villa'),
    ('Hotel','Hotel')
)

class Property(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="property_owner")
    type = models.CharField(max_length=40, choices=property_type)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
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

    created_date = models.DateField(auto_now_add=True)

    @property
    def all_images(self):
        return self.images.all()

    @property
    def all_orders(self):
        return self.booking.filter(checkout=False)

    @property
    def get_rules(self):

        return self.rules.split('\n')

    @property
    def get_review(self):
        return self.review.all()

    # @property
    # def get_booked_booking(self):
    #     return self.user_booking.all()

    @staticmethod
    def get_search_data(type, location, no_of_people):

        return Property.objects.filter(Q(city__icontains = location) | Q(address__icontains=location), available= True, type__iexact= type)





class PropertyImages(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to = 'property/other_images')



class PropertyReview(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.TextField()

    update_date = models.DateField(auto_now=True)


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug[:max_length-5], randstr = random_string_generator(size = 4))

        return unique_slug_generator(instance, new_slug = new_slug)
    return slug

@receiver(pre_save, sender=Property)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance:
        send_property_added_email(instance)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)