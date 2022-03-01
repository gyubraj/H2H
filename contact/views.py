from django.shortcuts import render
from django.views import View
from contact.models import Contact

class ContactView(View):

    def get(self, request):
        pass

    def post(self, request):

        if request.user.is_authenticated():
            email = request.user.email
            name = request.user.name
        else:
            email = request.POST['email']
            name = request.POST['name']
        
        message = request.POST['message']
        subject = request.POST['subject']

        Contact.objects.create(email= email, name= name, subject= subject, query= message)

        return "Thank you! we will reach too you as soon as possible."
