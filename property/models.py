from django.db import models
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
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


class PropertyImages(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'property/other_images')


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
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)