from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/login', views.LoginView.as_view(template_name="boec_core/user_base/login.html"), name="login"),
    path('user/logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    # path('boec/admin', views.AdminIndexView.as_view(), name="login"),
    path('boec/customer', views.CustomerIndexView.as_view(), name="main_customer"),
    path('boec/shopping-cart', views.CartView.as_view(), name="cart_view"),
    path('boec/checkout', views.CheckoutView.as_view(), name="checkout"),
    path('api/cart/add_product_to_cart', views.add_product_to_cart, name='add_product_to_cart'),

    path('', views.Index.as_view(), name='index')
]