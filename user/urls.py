""""""

from django.urls import path
from user.views import RegisterView, LoginView, ResetPasswordRequestView, ResetPasswordView, ActivateAccount, LogoutUser

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name= 'register'),
    path('request-reset-password/', ResetPasswordRequestView.as_view(),name='request-reset-password'),
    path('reset-password/<str:uid>/<str:token>/',ResetPasswordView.as_view(),name="reset-password"),
    path('activate-account/<str:uid>/<str:token>/',ActivateAccount.as_view(),name='activate-account'),
    path('logout',LogoutUser.as_view(), name="logout")
]