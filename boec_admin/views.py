from django.shortcuts import render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    oders = [1,2,3,4,5,6]
    return render(request, "common/oders.html", {"oders":oders} )
def productlist(request):
    return render(request, "common/productlist.html" )

def addProduct(request):
    name= request.GET['product_name']
    price = request.GET['price']
    quantity = request.GET['quantity']
    status = request.GET['status']
    discription =request.GET['disscription']

    category= Category( name='dien tu', desc='dat')
    category.save()
    Product.objects.create(name=name, desc = discription,category= category)
    return render(request, "common/productlist.html" )