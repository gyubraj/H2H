
from django.urls import path


from homepage.views import HomePage

urlpatterns = [
    path('',HomePage.as_view(),name='homepage'),
]