from django.shortcuts import redirect, render
from . models import categori,products,size,carts,address
# home page render.
def home_Render(request):
    categories = categori.objects.all()
    newproduct = products.objects.filter(pcat__lt=4).order_by("-id")[0:6]
    oldproducts = products.objects.filter(pcat__lt=4).order_by("-id")[6:18]
    hotdill = products.objects.filter(photdil=1).order_by("-id")
    return render(request,"home.html",{'categories':categories,'product':newproduct,"oldproducts":oldproducts,"hotdill":hotdill})

#show all products page render
def all_product(request):
    categories = categori.objects.all()
    allproducts = products.objects.filter(pcat__lt=4).order_by("-id")
    return render(request,"products.html",{'categories':categories,"allproducts":allproducts})

def protected_route(request):
     if(not request.session.get("id")):
        return redirect("Login_page")
     
     

#single product page rander
def Single_product(request,id):
    categories = categori.objects.all()
    singleProduct = products.objects.filter(id=id)
    for p in singleProduct:
        product = products.objects.filter(pcat=p.pcat)
       # product_size = size.objects.get(id=p.psize)
    return render(request,"product.html",{'categories':categories,'singleProduct':singleProduct,'product':product})

#Login  page rander
def Login_page(request):
    if(request.session.get("id")):
        return redirect('home')
    return render(request,"Login.html")

#Register  page rander
def Register_page(request):
    if(request.session.get("id")):
        return redirect('home')
    return render(request,"register.html")

#cart  page rander
def Cart_page(request):
     if(not request.session.get("id")):
        return redirect("Login_page")
     else:
       categories = categori.objects.all()
       cart_product=carts.objects.filter(user=request.session.get("id")).order_by("-id")
       return render(request,"carts.html",{'categories':categories,'cart':cart_product})

#Orders  page rander
def Orders_page(request):
    if(not request.session.get("id")):
        return redirect("Login_page")
    else:
       categories = categori.objects.all()
       
       return render(request,"orders.html",{'categories':categories})

#add_address  page rander
def Add_address_page(request):
    categories = categori.objects.all()
    addres=address.objects.filter(user=request.session.get("id")).order_by("-id")
    return render(request,"add_Address.html",{'categories':categories,'addres':addres})

#Payment  page rander
def Payment_page(request):
   if(not request.session.get("id")):
        return redirect("Login_page")
   else:
    if request.method == "POST":
      pid = request.POST.get("pid")
      psize=request.POST.get("psize")
      request.session["psize"]=psize
      request.session["pid"]=pid
      product = products.objects.filter(id=pid)
      categories = categori.objects.all()
      addres=address.objects.filter(user=request.session.get("id")).order_by("-id")
      return render(request,"payments.html",{'categories':categories,'addres':addres,'product':product})
    else:
        return redirect("home")

#grocary page render
def grocory_page(request):
    categories = categori.objects.all()
    grocory = products.objects.filter(pcat=4).order_by("-id")
    return render(request,"grocary.html",{'categories':categories,"grocory":grocory})