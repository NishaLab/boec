from django.shortcuts import render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    list_Order = Order.objects.all()
    # list_Amount = []
    # for oder in list_Order:    
    #     list_OrderProduct = OrderedProduct.objects.get(oder = oder.id)
    #     total = 0
    #     for item in list_OrderProduct:
    #         total += item.price
    #     list_Amount.append(total)
    return render(request, "common/oders.html", {"oders":list_Order} )

def detailOrder(request,order_id):
    products = OrderedProduct.objects.get(order = order_id)
    return render(request, 'common/detail_order.html')
    