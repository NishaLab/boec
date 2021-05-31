from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/login', views.LoginView.as_view(template_name="boec_core/user_base/login.html"), name="login"),
    path('user/logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    #path('boec/admin', views.AdminIndexView.as_view(), name="login"),

    path('', views.Index.as_view(), name='index')
]