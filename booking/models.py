from django.db import models
from django.db.models import Q
from django.db.models import Sum

from user.models import User
from property.models import Property

# Create your models here.


class Booking(models.Model):

    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name="booking")
    visitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    no_people = models.IntegerField()
    rooms = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.FloatField(null= True,blank=True)

    order_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:

        print("Hello World")
        total_rooms = self.property.total_rooms
        property_per_room_person = self.property.person_per_room
        price_per_room = self.property.price_per_room
        increase_price_per_person = self.property.increase_price_per_person
        order_rooms= self.rooms
        order_no_of_people = self.no_people


        if order_no_of_people > ( order_rooms * property_per_room_person):
            return "Not Valid Data"


        already_order_room = self.property.all_orders.filter(from_date__gte=self.from_date,to_date__lte=self.to_date).aggregate(od_room=Sum('rooms'))['od_room']
        if already_order_room and  already_order_room>0 and (total_rooms-already_order_room)< order_rooms:
            return "Not Available"
        
        self.price = (order_rooms*price_per_room)+(order_no_of_people-order_rooms)*increase_price_per_person
        
        super(Booking,self).save(*args,**kwargs)

