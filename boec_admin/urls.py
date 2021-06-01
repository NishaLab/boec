from django.urls import path
from . import views

urlpatterns = [
    path('boec/admin/',views.index, name='common'),
    path('boec/admin/oders/',views.oders, name='list_order'),
    path('boec/admin/oders/detail/<int:order_id>',views.detailOrder, name='detail_order')
]
