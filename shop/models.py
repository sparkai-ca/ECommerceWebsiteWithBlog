from django.db import models

# Create your models here.

class Product(models.Model):

    id=models.AutoField
    name=models.CharField(max_length=100, default="")
    description=models.CharField(max_length=500, default="")
    stock=models.IntegerField(default=0)
    supplier=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    url=models.CharField(max_length=300, default="static/shop/test.jpg")
    category=models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


# --------------------------------------------------------------------------------------------------------------------------------------------------------


class ContactUs(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=150,default="Default_Name")
    email=models.CharField(max_length=200, default="Default@gmail.com")
    phone=models.CharField(max_length=50, default="0000000000000")
    textarea=models.CharField(max_length=1000, default="Default_textarea")

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField
    items=models.CharField(max_length=500,default="No Item")
    ttl=models.CharField(max_length=20,default="total")
    name=models.CharField(max_length=50,default="order_name")
    email=models.CharField(max_length=100,default="order_email")
    address=models.CharField(max_length=300,default="order_address")
    country=models.CharField(max_length=50,default="order_country")
    city=models.CharField(max_length=50,default="order_city")
    state=models.CharField(max_length=50,default="order_state")
    zip=models.CharField(max_length=20,default="order_zip")
    phone=models.CharField(max_length=50,default="order_phone")

    def __str__(self):
        return self.name
