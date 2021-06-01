from django.urls import path
from . import views

urlpatterns = [
    path('boec/admin/',views.index),
    path('boec/admin/oders/',views.oders),
    path('productlist/',views.productlist, name="productlist"),
    path('add_product/',views.addProduct, name="addProduct"),
]
