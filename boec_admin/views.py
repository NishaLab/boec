from django.shortcuts import render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    list_Order = Order.objects.all()
    return render(request, "common/oders.html", {"oders":list_Order} )