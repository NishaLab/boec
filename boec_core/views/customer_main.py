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
        if 'cart' not in request.session:
            cart = []
        else:
            cart = request.session['cart']
        self.context["user"] = user
        self.context["featured_products"] = featured_products
        self.context["cart"] = len(cart)
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
        cart = {}
        cart_items = []
        total = 0
        if 'cart' not in request.session:
            cart = {}
        else:
            cart = request.session['cart']
        for item in cart:
            variant = ProductVariant.objects.get(pk=item)
            quantity = cart[item]
            amount = quantity * variant.price
            setattr(variant, 'quantity', quantity)
            setattr(variant, 'total', amount)
            total += amount
            cart_items.append(variant)
        self.context["cart"] = len(cart)
        self.context["cart_items"] = cart_items
        self.context["total"] = total

        return super().update_get_context(request, *args, **kwargs)

class CheckoutView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "boec_core/customer/checkout.html"

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        cart = {}
        cart_items = []
        total = 0
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("city")
        note = request.POST.get("note")
        order = Order(recv_name=name,recv_city=city,recv_phone=phone,
        recv_email=email,note=note,customer=user,payment_type="COD",shipping_address=address)
        order.save()
        if 'cart' not in request.session:
            cart = {}
        else:
            cart = request.session['cart']
        for item in cart:
            variant = ProductVariant.objects.get(pk=item)
            quantity = cart[item]
            amount = quantity * variant.price
            ordered_product = OrderedProduct(quantity=quantity, price=variant.price,
             order=order, product=variant)
            ordered_product.save()
        del request.session['cart']
        order.amount = total
        order.save()
        return HttpResponseRedirect("/boec/customer")

    def update_get_context(self, request, *args, **kwargs):
        user = request.user
        self.context["user"] = user
        cart = {}
        cart_items = []
        total = 0
        if 'cart' not in request.session:
            cart = {}
        else:
            cart = request.session['cart']
        for item in cart:
            variant = ProductVariant.objects.get(pk=item)
            quantity = cart[item]
            amount = quantity * variant.price
            setattr(variant, 'quantity', quantity)
            setattr(variant, 'total', amount)
            total += amount
            cart_items.append(variant)
        self.context["cart"] = len(cart)
        self.context["cart_items"] = cart_items
        self.context["total"] = total

        return super().update_get_context(request, *args, **kwargs)