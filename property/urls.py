

from django.urls import path

from property.views import AddPropertyView

urlpatterns = [ 
    path('add-property',AddPropertyView.as_view(),name='add-property'),
]