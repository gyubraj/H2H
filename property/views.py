from django.shortcuts import render
from django.views import View

# Create your views here.

class AddPropertyView(View):

    template_name = "property/addproperty.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request,"property/success.html")


class DeletePropertyView(View):

    def get(self, request, pk):
        pass



class MyProperty(View):

    def get(self, request):

        return render(request, "mylistings/myproperty.html")
