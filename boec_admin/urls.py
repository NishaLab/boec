from django.urls import path
from . import views

urlpatterns = [
    path('boec/admin/',views.index),
    path('boec/admin/oders/',views.oders)
]
