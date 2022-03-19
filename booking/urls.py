from unicodedata import name
from django.urls import path
from booking.views import ReceivedBookingView, BookedBookingView, AddBookingView, EditBookingView, DeleteBookingView, CheckoutBookView

urlpatterns = [
    path('received-booking',ReceivedBookingView.as_view(), name="received-booking"),
    path('my-booking',BookedBookingView.as_view(),name="booked-booking"),
    path('add-booking/<str:slug>',AddBookingView.as_view(), name= "add-booking"),
    path('edit-booking/<int:id>',EditBookingView.as_view(), name= "edit-booking"),
    path('delete-booking/<int:id>', DeleteBookingView.as_view(), name= "delete-booking"),
    path('checkout/<int:id>',CheckoutBookView.as_view(), name="checkout"),

]