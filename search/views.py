from django.shortcuts import render
from django.views import View
from property.models import Property, PropertyImages

# Create your views here.


class SearchView(View):

    def get(self,request):
        pass

    def post(self, request):

        location = request.POST['location']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        type = request.POST['type']

        property = Property.objects.filter(available= True, type__iexact = type, location__icontains = location)

        context = {
            'property': property
        }

        return render(request, 'search/search.html', context=context)






        
