
from django.urls import path
from . import views
from . import product
from . import users
from . import address
urlpatterns = [
   path('home/',views.home_Render,name="home"),
   #path('layout/',views.Layout),
   path('home/products',views.all_product,name="products"),
   path('home/products/singleProduct/<int:id>',views.Single_product,name="Single_product"),
   path('home/login',views.Login_page,name="Login_page"),
   path('home/Register',views.Register_page,name="Register_page"),
   path('home/Cart_page',views.Cart_page,name="Cart_page"),
   path('home/Orders_page',views.Orders_page,name="Orders_page"),
   path('home/Add_address_page',views.Add_address_page,name="Add_address_page"),
   path('home/Payment_page',views.Payment_page,name="Payment_page"),
   path('home/grocory_page',views.grocory_page,name="grocory_page"),

    #/////////////add to cart///////////////
   path('cart/',product.add_cart,name="cart"),
   path('delete/<int:id>',product.removecart,name="removecart"),

     #/////////////register user///////////////
   path('register/',users.register_user,name="register"),
   path('login_user/',users.login_user,name="login_user"),
   path('logout/',users.logout,name="logout"),

   #////address////////////
   path('add/address/',address.add_address,name="address"),
   path('delete/address/<int:id>',address.delete_address,name="address_delete"),
#///showcategories filter///
   path('filter/categories/<int:id>',product.categpryProduct,name="categpryProduct"),
   #search
   path('search/',product.searchProduct,name="search")
]