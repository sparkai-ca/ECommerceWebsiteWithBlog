from django.contrib import admin
from . models import Product,ContactUs,Order

# Register your models here.

admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(Order)