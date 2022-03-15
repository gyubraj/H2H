from unicodedata import name
from django.urls import path
from booking.views import BookingView, AddBookingView, EditBookingView, DeleteBookingView

urlpatterns = [
    path('',BookingView.as_view(), name="booking"),
    path('add-booking',AddBookingView.as_view(), name= "add-booking"),
    path('edit-booking/<int:id>',EditBookingView.as_view(), name= "edit-booking"),
    path('delete-booking', DeleteBookingView.as_view(), name= "delete-booking")

]