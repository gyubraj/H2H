from django.shortcuts import render, get_object_or_404

from django.views import View

from property.models import Property
# Create your views here.


class AddOrder(View):

    def get(self, request, slug):

        property = get_object_or_404(Property, slug= slug, available = True)

        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        no_of_people = request.POST['no_of_people']
        no_of_rooms = request.POST['no_of_rooms']

        



