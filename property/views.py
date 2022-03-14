from django.shortcuts import render, get_object_or_404
from django.views import View
from property.models import Property, PropertyImages
from user.models import User


# Create your views here.
class PropertyDetailView(View):

    def get(self,request,slug):
        property = get_object_or_404(Property,slug=slug)
        if request.user.is_authenticated:
            request.user.recommendFor = property.name
            request.user.save()
        context={
            'property':property
        }

        return render(request,'property/property_detail.html',context)


class AddPropertyView(View):

    template_name = "property/addproperty.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data={
            'owner': request.user,
            'type':request.POST['type'],
            'name': request.POST['name'],
            'total_rooms': request.POST['no_of_rooms'],
            'price_per_room': request.POST['price_per_room'],
            'person_per_room': request.POST['max_people_per_room'],
            'increase_price_per_person': request.POST['increase_price_per_person'],
            'complementary_breakfast': request.POST.get('breakfast','') == "on",
            'luxirous_room': request.POST.get('luxrious_room','') == "on",
            'attached_bathroom': request.POST.get('bathroom','') == "on",
            'hot_shower': request.POST.get('shower','') == "on",
            'tv': request.POST.get('tv','') == "on",
            'ac': request.POST.get('ac','') == "on",
            'internet': request.POST.get('internet','') == "on",
            'smoking_drinking': request.POST.get('smoking','') == "on",
            'receive_facility': request.POST.get('receive_facility','') == "on",
            'drop_facility': request.POST.get('drop_facility','') == "on",
            'city': request.POST['city'],
            'address': request.POST['address'],
            'nearest_landmark': request.POST['landmark'],
            'rules': request.POST['rules'],
            'main_image': request.FILES['room_image']
        }
        property = Property.objects.create(**data)
        other_images = request.FILES.getlist('other_images')
        for img in other_images:
            PropertyImages.objects.create(property=property,image=img)
        return render(request,"property/success.html")


class EditProperty(View):
    template_name = "property/editproperty.html"

    def get(self,request, slug):
        property = get_object_or_404(Property, slug=slug, user= request.user)
        images = PropertyImages.objects.filter(property = property)
        context = {
            'property': property,
            'propertyimages': images
        }
        return render(request, self.template_name,context= context)

    def post(self, request, slug):

        property = get_object_or_404(Property, slug=slug, user= request.user)

        property.name = request.POST['name']
        property.type = request.POST['type']
        property.total_rooms = request.POST['no_of_rooms']
        property.price_per_room = request.POST['price_per_room']
        property.person_per_room = request.POST['max_people_per_room']
        property.increase_price_per_person = request.POST['increase_price_per_person']
        property.complementary_breakfast = request.POST.get('breakfast','') == "on"
        property.luxirous_room = request.POST.get('luxrious_room','') == "on"
        property.attached_bathroom = request.POST.get('bathroom','') == "on"
        property.hot_shower = request.POST.get('shower','') == "on"
        property.tv = request.POST.get('tv','') == "on"
        property.ac = request.POST.get('ac','') == "on"
        property.internet = request.POST.get('internet','') == "on"
        property.smoking_drinking = request.POST.get('smoking','') == "on"
        property.receive_facility = request.POST.get('receive_facility','') == "on"
        property.drop_facility = request.POST.get('drop_facility','') == "on"
        property.city = request.POST['city']
        property.address = request.POST['address']
        property.nearest_landmark = request.POST['landmark']
        property.rules = request.POST['rules']
        property.main_image = request.FILES['room_image']

        property.save()

        return render(request,"property/editsuccess.html")



class DeletePropertyView(View):

    def get(self, request, slug):
        property = get_object_or_404(Property, slug= slug, user= request.user)

        property.delete()

        return render(request,"property/deletesuccess.html")


# TODO
class ChangePropertyAvailable(View):

    def get(self, request, slug):

        property = get_object_or_404(Property, user = request.user, slug= slug)

        property.available = request.POST['available']
        



class MyProperty(View):

    def get(self, request):

        property = Property.objects.filter(owner=request.user)

        context ={
            'property':property
        }

        return render(request, "mylistings/myproperty.html",context=context)

