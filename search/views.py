from django.shortcuts import render
from django.views import View

# Create your views here.


class SearchView(View):

    def get(self,request):
        pass

    def post(self, request):

        location = request.POST['location']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        type = request.POST['type']

        
