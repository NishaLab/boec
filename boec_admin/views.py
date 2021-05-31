from django.shortcuts import render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    oders = [1,2,3,4,5,6]
    return render(request, "common/oders.html", {"oders":oders} )