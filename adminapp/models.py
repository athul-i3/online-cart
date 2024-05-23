from django.db import models


# Create your models here.
class Admincat(models.Model):
    cat_image = models.ImageField(upload_to='cat',default='sample.jpg')
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name

class Products(models.Model):
    Cat_id=models.ForeignKey(Admincat,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='products')
    product_name=models.CharField(max_length=30,null=True)
    brand_name = models.CharField(max_length=25)
    product_price = models.IntegerField(null=True)
    product_disc = models.CharField(max_length=20)
    product_warranty = models.CharField(max_length=20,null=True)
    product_delivery = models.CharField(max_length=20,null=True)
    product_rate= models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.product_name
    

class Notification(models.Model):
    mess_title=models.CharField(max_length=20)
    mess_discription=models.TextField()
    time=models.DateTimeField(auto_now_add=True,null=True)
    
class Customer(models.Model):
    username=models.CharField(max_length=25)
    phonenumber=models.TextField()
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
  
class Cart(models.Model):
    userid =models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid =models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(null=True)
    total=models.FloatField(null=True)
    
class Contacts(models.Model):
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    discription=models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,null=True)

class Review(models.Model):   
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    productid =models.ForeignKey(Products,on_delete=models.CASCADE)
    add_review=models.CharField(max_length=200)

 
class Checkout(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    building_name=models.CharField(max_length=200)
    road_name=models.CharField(max_length=200)

class Wishlist(models.Model):
    userid =models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid =models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

