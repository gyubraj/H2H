from django.shortcuts import redirect, render
from django.views import View
from contact.models import Contact

class ContactView(View):

    def get(self, request):
        return redirect('homepage')

    def post(self, request):

        if request.user.is_authenticated:
            email = request.user.email
            name = request.user.name
        else:
            email = request.POST['email']
            name = request.POST['name']
        
        message = request.POST['message']
        subject = request.POST['subject']

        Contact.objects.create(email= email, name= name, subject= subject, query= message)

        return redirect('homepage')
