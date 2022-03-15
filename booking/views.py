from django.shortcuts import redirect, render, get_object_or_404

from django.views import View
from booking.models import Booking

from property.models import Property
# Create your views here.


class BookedBookingView(View):

    def get(self,request):

        booked = request.user.get_booked_booking


class ReceivedBookingView(View):

    def get(self, request):
        property = self.user.get_property

        context = {
            'property': property
        }

        return render(request, 'booking/bookingview.html', context=context)


class AddBookingView(View):

    def get(self, request, slug):

        return

    def post(self, request, slug):

        property = get_object_or_404(Property, slug= slug, available = True)

        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        no_of_people = request.POST['no_of_people']
        no_of_rooms = request.POST['no_of_rooms']

        data= {
            'property': property,
            'visitor': request.user,
            'no_people': no_of_people,
            'rooms': no_of_rooms,
            'from_date': from_date,
            'to_date' : to_date
        }

        booking = Booking.objects.create(**data)

        return redirect('homepage')

class EditBookingView(View):
    def get(self, request,id):

        return 

    def post(self, request, id):

        booking = get_object_or_404(Booking, pk=id, visitor=request.user)

        booking.from_date = request.POST['from_date']
        booking.to_date = request.POST['to_date']
        booking.no_people = request.POST['no_of_people']
        booking.rooms = request.POST['no_of_rooms']

        booking.save()

        return redirect('homepage')

        
class DeleteBookingView(View):

    def get(self, request, id):

        booking = get_object_or_404(Booking, pk=id, visitor=request.user)
        booking.delete()

        return redirect('homepage')
        




