from django.shortcuts import redirect, render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    list_Order = Order.objects.all()
    
    return render(request, "common/oders.html", {"oders":list_Order} )

def detailOrder(request,order_id):
    order = Order.objects.filter(id = order_id)
    products = OrderedProduct.objects.filter(order = order_id)
    return render(request, 'common/detail_order.html',{'products':products, 'order':order})

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

def changeStatusOrder(request, order_id):
    order = Order.objects.get(pk = order_id)
    value = request.POST["choice"]
    order.status = value
    order.save()
    listOrder = Order.objects.all()
    return render(request, 'common/oders.html', {"oders":listOrder})
