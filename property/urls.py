

from django.urls import path

from property.views import AddPropertyView, MyProperty, PropertyDetailView

urlpatterns = [ 
    path('add-property',AddPropertyView.as_view(),name='add-property'),
    path('my-property',MyProperty.as_view(),name='my-property'),
    path('property-detail/<str:slug>',PropertyDetailView.as_view(),name="property-detail"),
]