

from django.urls import path

from property.views import AddPropertyView, MyProperty

urlpatterns = [ 
    path('add-property',AddPropertyView.as_view(),name='add-property'),
    path('my-property',MyProperty.as_view(),name='my-property'),
]