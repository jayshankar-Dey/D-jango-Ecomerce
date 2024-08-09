from django.shortcuts import redirect, render
from . models import address


def add_address(request):
    pin=request.POST.get("pin")
    city=request.POST.get("city")
    addres=request.POST.get("address")
    user=request.session.get("id")

    address.objects.create(pin=pin,city=city,addres=addres,user=user),
    return redirect("home")
#delete address
def delete_address(request,id):
    address.objects.filter(id=id).delete()
    return redirect("Add_address_page")