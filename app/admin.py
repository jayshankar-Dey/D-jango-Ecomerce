from django.contrib import admin
from . models import size,products,categori,users,carts,address,order

class SIZE(admin.ModelAdmin):
    list_display = ("id","product_size1","product_size2","product_size3","product_size4")
class PRODUCTS(admin.ModelAdmin):
    list_display = ("id","pimage","pname","pdes","psize","ptotal","pprice","pdiscount","photdil")
class CATEGORI(admin.ModelAdmin):
    list_display = ("id","cname")
class USERS(admin.ModelAdmin):
    list_display = ("id","email","password")
class CARTS(admin.ModelAdmin):
    list_display=("id","user","image","pid","psize","created_at")

class ORDER(admin.ModelAdmin):
    list_display=("id","user","image","pid","psize","addres","created_at")
class ADDRESS(admin.ModelAdmin):
    list_display=("id","pin","city","addres","user")
# Register your models here.
admin.site.register(address,ADDRESS)
admin.site.register(order,ORDER)
admin.site.register(carts,CARTS)
admin.site.register(users,USERS)
admin.site.register(size,SIZE)
admin.site.register(products,PRODUCTS)
admin.site.register(categori,CATEGORI)
