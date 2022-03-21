from django.shortcuts import render
from django.views import View
from recommendationsystem.recommendation import initRecommend
import pandas as pd
# from django.db import connection
from user.models import User
from property.models import Property

class HomePage(View):

    def get(self,request):

        if request.user.is_authenticated:
            property = Property.objects.exclude(owner=request.user)
        else:
            property = Property.objects.all()

        recommendedPlace = None

        if request.user.is_authenticated and request.user.recommendFor:
            recommendedPlaces=initRecommend(request.user.recommendFor)
            querySet=Property.objects.in_bulk(recommendedPlaces)
            recommendedPlace=[querySet[recom] for recom in recommendedPlaces]

        context={
            'homestay': property.filter(type__iexact='homestay')[:6],
            'villa': property.filter(type__iexact="villa")[:6],
            'hotel': property.filter(type__iexact = "hotel")[:6],
            'recommended': recommendedPlace
        }
        return render(request,'homepage/homepage.html',context=context)
