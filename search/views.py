from django.shortcuts import redirect, render
from django.views import View
from property.models import Property

# Create your views here.


class SearchView(View):

    def get(self,request):
        return redirect('homepage')

    def post(self, request):

        location = request.POST['location']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        type = request.POST['type']
        no_of_people = int(request.POST['no_of_people'])

        property = Property.get_search_data(type=type, location=location, no_of_people=no_of_people)

        context = {
            'property': property,
            'location':location,
            'start_date':start_date,
            'end_date': end_date,
            'type': type
        }

        return render(request, 'search/searchs.html', context=context)






        
