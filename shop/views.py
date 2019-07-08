from django.shortcuts import render
from .models import Product,ContactUs,Order
from .supports import categories,cart_list
import numpy as np

# Create your views here

def shop_index(request):

    if(len(cart_list._list)==0):

        list0 = Product.objects.values()

        prods=[]
        for p in list0:
            prods.append(list(p.values()))

        categories.cats = list(set(i[7] for i in prods))

        for i in categories.cats:
            cart_list._list[i]=[]

        for key,value in cart_list._list.items():
            for p in prods:
                if p[7] == key:
                    value.append(p)

    params = {'lists': cart_list._list.items()}
    return render(request, 'shop/shop_index.html', params)

def shop_aboutus(request):
    params={'dummy': 'Mujahid'}
    return render(request, 'shop/shop_aboutus.html',params)

def shop_contactus(request):

    name=request.POST.get("name",'Default_name')
    email=request.POST.get("email",'Default_email')
    phone=request.POST.get("phone",'Default_phone')
    textarea=request.POST.get("textarea",'Default_textarea')

    contact=ContactUs(name=name,email=email,phone=phone,textarea=textarea)
    contact.save()

    return render(request, 'shop/shop_contactus.html')

def shop_tracker(request):
    params={'dummy': 'Tracker'}
    return render(request, 'shop/shop_tracker.html',params)

def shop_cart(request, items):

    _items_=items.split(',')

    items=_items_

    _list=[]

    list0 = Product.objects.values()
    prods = []
    for p in list0:
        prods.append(list(p.values()))

    for i in items:
        for p in prods:
            if int(i) == int(p[0]):
                _list.append(p)

    params={'list':_list}
    return render(request,'shop/shop_cart.html',params)

def shop_checkout(request, items):

    _items_=items.split(',')

    items=_items_

    _list=[]

    list0 = Product.objects.values()
    prods = []
    for p in list0:
        prods.append(list(p.values()))

    for i in items:
        for p in prods:
            if int(i) == int(p[0]):
                _list.append(p)

    params={'list':_list}
    return render(request,'shop/shop_checkout.html',params)

def shop_product(request,id):

    c,i=str.split(id,",")

    cat=str(c)
    _id=str(i)

    prods = cart_list._list.items()

    _list0 = []

    for key,value in prods:
        if cat==key:
            for p in value:
                if(str(_id) == str(p[0])):
                    for i in p:
                        _list0.append(i)
                    print(_list0)

    return render(request, 'shop/shop_product.html',{'list':_list0})


def shop_payment(request):
    print('payment')
    return render(request, 'shop/shop_payment.html')


def shop_pay(request):

    items = request.GET.get("items", 'No Item')
    ttl = request.GET.get("ttl", 'Default_Total')
    name = request.GET.get("name", 'Default_name')
    email = request.GET.get("email", 'Default_email')
    address = request.GET.get("address", 'Default_address')
    country = request.GET.get("country", 'Default_country')
    city = request.GET.get("city", 'Default_city')
    state = request.GET.get("state", 'Default_state')
    zip = request.GET.get("zip", 'Default_zip')
    phone = request.GET.get("phone", 'Default_phone')

    order = Order(items=items,ttl=ttl,name=name,email=email,address=address,country=country,city=city,state=state,zip=zip,phone=phone)
    order.save()

    return render(request, 'shop/shop_pay.html',{'items':items,'ttl':ttl, 'name':name,'email':email,'address':address,'country':country,'city':city,'state':state,'zip':zip,'phone':phone})
