from django.urls import path
from . import views

urlpatterns = [
    path('boec_admin/',views.index, name='common'),
    path('boec_admin/oders/',views.oders, name='list_order'),
    path('boec_admin/edit_status/<int:order_id>',views.changeStatusOrder, name='changeStatus'),
    path('boec_admin/oders/detail/<int:order_id>',views.detailOrder, name='detail_order'),
    path('boec_admin/productlist/',views.productlist, name="productlist"),
    path('boec_admin/add_product/',views.addProduct, name="addProduct"),
    path('boec_admin/edit_product/',views.editProduct, name="editProduct"),
]
