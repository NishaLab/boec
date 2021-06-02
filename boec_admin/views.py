from django.shortcuts import redirect, render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    list_Order = Order.objects.all()
    list_Amount = []
    for item in list_Order:    
        list_OrderProduct = OrderedProduct.objects.filter(order = item.id)
        total = 0
        for item in list_OrderProduct:
            total += item.price
        list_Amount.append(total)
    return render(request, "common/oders.html", {"oders":list_Order,"amount":list_Amount} )

def detailOrder(request,order_id):
    order = Order.objects.get(pk = order_id)
    products = OrderedProduct.objects.filter(order = order_id)
    return render(request, 'common/detail_order.html',{'products':products, 'order':order})
    
    oders = [1,2,3,4,5,6]
    return render(request, "common/oders.html", {"oders":oders} )

def productlist(request):
    products = Product.objects.all()
    return render(request, "common/productlist.html",{'products':products})

def addProduct(request):
    name= request.GET['product_name']
    price = request.GET['price']
    quantity = request.GET['quantity']
    status = request.GET['status']
    discription =request.GET['disscription']

    category= Category( name='dien tu', desc='dat')
    category.save()
    Product.objects.create(name=name, desc = discription,category= category)
    data = Product.objects.all()
    return redirect('productlist')

def editProduct(request):
    return render(request, "common/productEdit.html")
