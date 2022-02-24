from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from user.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from user.utils import activate_account

class RegisterView(View):

    template_name = "user/register.html"

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        try:
            User.objects.create_user(email,name,password)
        except:
            
            return HttpResponse("<h1>There seems to be an error</h1>")
        return redirect('login')

class LoginView(View):

    template_name = "user/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        return redirect('login')




class ResetPasswordRequestView(View):

    template_name = "user/reset_password_request.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        
        email = request.POST['email']


class ResetPasswordView(View):

    template_name = "user/reset_password.html"

    def get(self, request, uid, token):

        return render(request, self.template_name)

    def post(self, request, uid, token):
        pass

        


class ActivateAccount(View):

    def get(self,request, uid, token):

        if activate_account(uid,token):
            return redirect('login')

        return redirect('register')




