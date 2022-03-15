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

        property = Property.get_search_data(type=type, location=location)

        context = {
            'property': property,
            'location':location,
            'start_date':start_date,
            'end_date': end_date
        }

        return render(request, 'search/search.html', context=context)






        
