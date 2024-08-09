from django.db import models

# Create your models here.

class size(models.Model):
    product_size1 = models.CharField(max_length=200,null=True)
    product_size2 = models.CharField(max_length=200,null=True)
    product_size3 = models.CharField(max_length=200,null=True)
    product_size4 = models.CharField(max_length=200,null=True)

    

class categori(models.Model):
    cname = models.CharField(max_length=200)

    def __str__(self):
       return self.cname

class products(models.Model):
    pimage=models.ImageField(upload_to="images/")
    pname = models.CharField(max_length=240)
    pdes = models.TextField(null=True)
    psize = models.ForeignKey(size,blank=True,default = 0, related_name='missions_assigned',null=True,on_delete=models.CASCADE)
    ptotal = models.FloatField(null=True)
    pprice = models.FloatField(null=True)
    pdiscount = models.CharField(max_length=40)
    photdil = models.IntegerField(null=True,default=0)
    pcat = models.ForeignKey(categori,null=True,on_delete=models.CASCADE)

class users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length = 200)

class carts(models.Model):
    user=models.IntegerField()
    image=models.CharField(max_length=240)
    pid=models.ForeignKey(products, on_delete=models.CASCADE)
    psize=models.CharField(null=True,blank=True ,max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class address(models.Model):
    user=models.IntegerField(null=True)
    pin=models.CharField(max_length=240)
    city=models.CharField(max_length=240)
    addres=models.CharField(max_length=240)

class order(models.Model):
    user=models.IntegerField(null=True)
    image=models.CharField(max_length=240)
    pid=models.ForeignKey(products, on_delete=models.CASCADE)
    psize=models.CharField(null=True,blank=True ,max_length=50)
    addres=models.ForeignKey(address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)