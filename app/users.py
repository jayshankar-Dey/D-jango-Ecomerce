from . models import users
from django.shortcuts import redirect, render
from django.contrib import messages

# register user/////////////////
def register_user(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    request.session["name"] =name
    request.session["email"] =email
    request.session["password"] =password
    if(name and email and password):
       if(users.objects.filter(email=email)):
           return redirect("Register_page")
       else:
           users.objects.create(name=name,email=email,password=password)
    else:
        return redirect("Register_page")
    return redirect("Login_page")

# login user //////////////////////

def login_user(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    request.session["name"] =""
    request.session["email"] =""
    request.session["password"] =""
    print(email,password)
    if(email and password):
        user = users.objects.filter(email=email,password=password)
        if(user):
            for user in user:
                request.session["user"] = user.name
                request.session["id"] = user.id
                return redirect("home")
        else:
            return redirect("Login_page")
    else:
        return redirect("Login_page")
#logout user
def logout(request):
    request.session["user"] = ""
    request.session["id"] = ""
    return redirect("Login_page")