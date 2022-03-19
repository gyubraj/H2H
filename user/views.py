from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from user.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from user.utils import activate_account, send_password_reset_email


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
            messages.add_message(request, message="Looks like this email is already registered.",level=messages.ERROR)
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
        
        messages.add_message(request, message="Enter valid email and Password.",level=messages.ERROR)

        return redirect('login')




class ResetPasswordRequestView(View):

    template_name = "user/reset_password_request.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        
        email = request.POST['email']

        try:
            user = User.objects.get(email__iexact = email)
            send_password_reset_email(user)
        except:
            messages.add_message(request, message="Something went wrong.",level=messages.ERROR)

        return redirect('login')


class ResetPasswordView(View):

    template_name = "user/reset_password.html"

    def get(self, request, uid, token):

        return render(request, self.template_name)

    def post(self, request, uid, token):
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return redirect(reverse('reset-password', args=(uid,token)))

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception:
            user = None

        if user is not None and PasswordResetTokenGenerator().check_token(
            user, token
        ):
            user.set_password(password1)
            user.save()

            return redirect('login')
        
        return redirect(reverse('reset-password', args=(uid,token)))


class ActivateAccount(View):

    def get(self,request, uid, token):

        if activate_account(uid,token):
            return redirect('login')

        return redirect('register')


class LogoutUser(View):

    def get(self, request):

        logout(request)

        return redirect('login')



class ChangePasswordView(View):

    def get(self,request):

        return redirect('homepage')

    def post(self,request):

        password1 = request.POST['password1']

        password2 = request.POST['password2']

        if password1 != password2:

            return "Error"

        user = request.user

        user.set_password(password1)

        user.save()

        return redirect('homepage')

