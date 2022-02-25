from django.db import models
from user.models import User

# Create your models here.


class Booking(models.Model):

    property = models.ForeignKey(User,on_delete=models.CASCADE)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    no_people = models.IntegerField()
    rooms = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    order_date = models.DateTimeField(auto_now=True)

