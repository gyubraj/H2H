from django.shortcuts import render
from django.views import View

# Create your views here.


class RegisterView(View):

    template_name = "user/register.html"

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']


class LoginView(View):

    template_name = "user/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

# class ResendVerificationLinkView(View):

#     template_name = "user/resendverification.html"

#     def get


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

        return 

