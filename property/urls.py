

from unicodedata import name
from django.urls import path

from property.views import AddPropertyView, MyProperty, PropertyDetailView, EditProperty, DeletePropertyView, PropertyReviewView

urlpatterns = [ 
    path('add-property',AddPropertyView.as_view(),name='add-property'),
    path('edit-property/<str:slug>',EditProperty.as_view(),name="edit-property"),
    path('my-property',MyProperty.as_view(),name='my-property'),
    path('property-detail/<str:slug>',PropertyDetailView.as_view(),name="property-detail"),
    path('delete-property/<str:slug>',DeletePropertyView.as_view(),name="delete-property"),
    path('submit-review/<str:slug>',PropertyReviewView.as_view(),name="submit-review"),
    
]