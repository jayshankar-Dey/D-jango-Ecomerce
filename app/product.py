from django.shortcuts import redirect, render
from . models import carts,products,categori
def add_cart(request):
    if(not request.session.get("id")):
        return redirect("Login_page")
    
    user=request.POST.get("user")
    image=request.POST.get("image")
    pid=int(request.POST.get("pid"))
    product = products.objects.get(id=pid)
    psize=request.POST.get("psize")
    
    carts.objects.create(user=user,image=image,pid=product,psize=psize)
    return redirect("Cart_page")

def removecart(request,id):
    carts.objects.get(id=id).delete()
    return redirect("Cart_page")

def categpryProduct(request,id):
    categories = categori.objects.all()
    allproducts = products.objects.filter(pcat=id)
    return render(request,"cateriesProduct.html",{'categories':categories,"allproducts":allproducts})

def searchProduct(request):
    search=request.POST.get("search")
    categories = categori.objects.all()
    allproducts = products.objects.filter(pname__contains=search).exclude(pcat =4)|products.objects.filter(pdes__contains=search).exclude(pcat =4)
    return render(request,"search.html",{'categories':categories,"allproducts":allproducts})
