from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from django.views import View
from booking.models import Booking

from property.models import Property

from dateutil import parser
# Create your views here.


class BookedBookingView(View):

    def get(self,request):

        bookedproperty = request.user.get_booked_booking
        context = {
            'property' : bookedproperty
        }

        return render(request, "booking/bookedview.html", context=context)


class ReceivedBookingView(View):

    def get(self, request):
        property = request.user.get_property

        context = {
            'property': property
        }

        return render(request, 'booking/receivedview.html', context=context)


class AddBookingView(View):

    def get(self, request, slug):

        return redirect('homepage')

    def post(self, request, slug):


        print("Hello World")

        property = get_object_or_404(Property, slug= slug, available = True)

        if property.owner == request.user:

            return HttpResponse("<h1>You can't Book your own Property </h1>")

        from_date = parser.parse(request.POST['from_date'])
        to_date = parser.parse(request.POST['to_date'])
        no_of_people = int(request.POST['no_of_people'])
        no_of_rooms = int(request.POST['no_of_rooms'])

        if Booking.objects.filter(from_date__gte=from_date, to_date__lte = to_date, property=property, visitor= request.user).exists():
            return HttpResponse("You Already have booked this property.")

        data= {
            'property': property,
            'visitor': request.user,
            'no_people': no_of_people,
            'rooms': no_of_rooms,
            'from_date': from_date,
            'to_date' : to_date
        }

        booking = Booking.objects.create(**data)

        return redirect('booked-booking')

class EditBookingView(View):
    def get(self, request,id):

        return redirect('homepage')

    def post(self, request, id):

        booking = get_object_or_404(Booking, pk=id, visitor=request.user)

        booking.from_date = parser.parse(request.POST['from_date'])
        booking.to_date = parser.parse(request.POST['to_date'])
        booking.no_people = int(request.POST['no_of_people'])
        booking.rooms = int(request.POST['no_of_rooms'])
        booking.save()

        return redirect('booked-booking')

        
class DeleteBookingView(View):

    def get(self, request, id):

        booking = get_object_or_404(Booking, pk=id, visitor=request.user)
        booking.delete()

        return redirect('booked-booking')
        




