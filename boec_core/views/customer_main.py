from .views import *
from django.contrib.auth import views as auth_views
import code; 

class CustomerIndexView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "boec_core/customer/index.html"

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def update_get_context(self, request, *args, **kwargs):
        user = request.user
        featured_products = ProductVariant.objects.filter(is_selling=True, is_feature=True)[:6]
        self.context["user"] = user
        self.context["featured_products"] = featured_products
        return super().update_get_context(request, *args, **kwargs)

class CartView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "boec_core/customer/shoping-cart.html"

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def update_get_context(self, request, *args, **kwargs):
        user = request.user
        self.context["user"] = user
        return super().update_get_context(request, *args, **kwargs)