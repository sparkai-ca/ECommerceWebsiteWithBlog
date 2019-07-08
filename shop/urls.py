from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shop_admin/', admin.site.urls),
    path('', views.shop_index, name='shop_home'),
    path('shop/aboutus/', views.shop_aboutus, name='shop_aboutus'),
    path('shop/contactus/', views.shop_contactus, name='shop_contactus'),
    path('shop/tracker/', views.shop_tracker, name='shop_tracker'),
    path('shop/product/<str:id>', views.shop_product, name='shop_product'),
    path('shop/cart/<str:items>', views.shop_cart, name='shop_cart'),
    path('shop/checkout/<str:items>', views.shop_checkout, name='shop_checkout'),
    path('shop/payment/', views.shop_payment, name='shop_payment'),
    path('shop/pay/', views.shop_pay, name='shop_pay'),


]

