from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import AnonymousUser
from datetime import timedelta, date
import code; 

class CustomerIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        featured_products = ProductVariant.objects.filter(is_selling=True, is_feature=True)[:6]
        for product in featured_products:
            options = VariantOption.objects.filter(product_id=product.id)
            setattr(product,"option", options.first().id)
        electronic_category = Category.objects.get(pk=1)
        electronic_subcategories = SubCategory.objects.filter(parent=electronic_category)
        for subcategory in electronic_subcategories:
            products = ProductVariant.objects.distinct().filter(is_selling=True,product__sub_category__id=subcategory.id)
            for product in products:
                options = VariantOption.objects.filter(product_id=product.id)
                setattr(product,"option", options.first().id)
            setattr(subcategory, "products", products)

        clothing_category = Category.objects.get(pk=3)
        clothing_subcategories = SubCategory.objects.filter(parent=clothing_category)
        for subcategory in clothing_subcategories:
            products = ProductVariant.objects.distinct().filter(is_selling=True,product__sub_category__id=subcategory.id)
            for product in products:
                options = VariantOption.objects.filter(product_id=product.id)
                setattr(product,"option", options.first().id)            
            setattr(subcategory, "products", products)

        book_category = Category.objects.get(pk=2)
        book_subcategories = SubCategory.objects.filter(parent=book_category)
        for subcategory in book_subcategories:
            products = ProductVariant.objects.distinct().filter(is_selling=True,product__sub_category__id=subcategory.id)
            for product in products:
                options = VariantOption.objects.filter(product_id=product.id)
                setattr(product,"option", options.first().id)
            setattr(subcategory, "products", products)

        if 'cart' not in request.session:
            cart = []
        else:
            cart = request.session['cart']
        if user.is_authenticated:
            context["user_id"] = user
            context["favorite"] = Favorite.objects.filter(customer=user).count()
        context["featured_products"] = featured_products
        context["electronic_subcategories"] = electronic_subcategories
        context["clothing_subcategories"] = clothing_subcategories
        context["book_subcategories"] = book_subcategories

        context["cart"] = len(cart)
        return render(request, "boec_core/customer/index.html",context)

class CartView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        context["user"] = user
        cart = {}
        cart_items = []
        total = 0
        if 'cart' not in request.session:
            cart = {}
        else:
            cart = request.session['cart']
        for item in cart:
            variant = VariantOption.objects.get(pk=item)
            quantity = cart[item]
            amount = quantity * variant.price
            setattr(variant, 'quantity', quantity)
            setattr(variant, 'total', amount)
            total += amount
            cart_items.append(variant)
        context["cart"] = len(cart)
        context["cart_items"] = cart_items
        context["total"] = total

        return render(request, "boec_core/customer/shoping-cart.html",context)

class FavoriteView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        favorites = Favorite.objects.filter(customer=user)
        featured_products = []
        for favorite in favorites:
            featured_products.append(favorite.product)
        
        if 'cart' not in request.session:
            cart = []
        else:
            cart = request.session['cart']
        if user.is_authenticated:
            context["user_id"] = user
            context["favorite"] = Favorite.objects.filter(customer=user).count()
        context["featured_products"] = featured_products
        context["cart"] = len(cart)
        return render(request, "boec_core/customer/favorite.html",context)

class ShopGridView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        search = request.GET.get("search")
        if search is None:
            selling_products = ProductVariant.objects.filter(is_selling=True)
        else:
            selling_products = ProductVariant.objects.distinct().filter(is_selling=True, product__name__icontains=search)

        if 'cart' not in request.session:
            cart = []
        else:
            cart = request.session['cart']
        if user.is_authenticated:
            favorites = Favorite.objects.filter(customer=user)
            context["user_id"] = user
            context["favorite"] = Favorite.objects.filter(customer=user).count()
        context["selling_products"] = selling_products
        context["cart"] = len(cart)
        page_size = settings.PAGE_SIZE
        page_num = request.GET.get("page_num")
        p = Paginator(selling_products, page_size)
        cur_page = p.page(1)
        if page_num is not None:
            cur_page = p.page(page_num)
        
        context["num_pages"] = p.num_pages
        context["pages"] = range(1, p.num_pages+1)
        return render(request, "boec_core/customer/shop-grid.html",context)
class VariantDetailView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        variant_id = kwargs.get('variant_id')
        variant = ProductVariant.objects.get(pk=variant_id)
        options = VariantOption.objects.filter(product=variant)
        reviews = CustomerReview.objects.filter(product=variant)
        recommend_products = ProductVariant.objects.filter(is_selling=True, is_feature=True)[:6]
        if 'cart' not in request.session:
            cart = []
        else:
            cart = request.session['cart']
        if user.is_authenticated:
            context["user_id"] = user
            context["favorite"] = Favorite.objects.filter(customer=user).count()
        rating = 0
        for review in reviews:
            rating += review.rating
            replies = Reply.objects.filter(review=review)
            setattr(review, "replies", replies)
        
        if reviews.count() == 0:
            rating = 0
            context["is_float"] = False
        else:
            rating = rating/reviews.count()
            if(rating%1!=0):
                context["is_float"] = True
        context["cart"] = len(cart)
        context["variant"] = variant
        context["options"] = options
        context["reviews"] = reviews
        context["price"]   = options.first().price
        context["ratings"] = int(rating)
        context["max_rating"] = [1,2,3,4,5]
        context["current_rating"] = [1] * int(rating)
        return render(request, "boec_core/customer/shop-details.html",context)

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        return render(request, "boec_core/customer/success_page.html",context)

class FailureView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        return render(request, "boec_core/customer/failure_page.html",context)
class FailureVoucherView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        return render(request, "boec_core/customer/failure_voucher.html",context)
class CheckoutView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart = {}
        cart_items = []
        total = 0
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        # L???y c??c th??ng tin ???????c g???i qua post request
        city = int(request.POST.get("city"))
        district = int(request.POST.get("district"))
        street = int(request.POST.get("street"))
        department = int(request.POST.get("department"))
        voucher = request.POST.get("voucher")
        detail = request.POST.get("detail")
        city = City.objects.get(pk=city)
        district = District.objects.get(pk=district)
        street = Street.objects.get(pk=street)
        department = ShippingDepartment.objects.get(pk=department)
        has_voucher = voucher
        voucher = Voucher.objects.filter(code=voucher).first()
        note = request.POST.get("note")
        # hi???n t???i ch??a c?? api l???Y gi?? v???n chuy???N -> m???c ?????nh gi?? v???N chuy???n l?? 30
        shipping_fee = 30
        # n???u user ????ng nh???p
        if voucher is None and has_voucher is not None:
            return HttpResponseRedirect("/boec/failure_voucher")
        if user.is_authenticated:
            order = Order(recv_name=name,recv_city=city, recv_district = district, recv_street=street, recv_house=detail, recv_phone=phone,
            recv_email=email,note=note,customer=user,payment_type="COD")
        else:
            order = Order(recv_name=name,recv_city=city, recv_district = district, recv_street=street, recv_house=detail,recv_phone=phone,
            recv_email=email,note=note,payment_type="COD")
        try:
            order.save()
            if 'cart' not in request.session:
                cart = {}
            else:
                cart = request.session['cart']
            for item in cart:
                variant = VariantOption.objects.get(pk=item)
                quantity = cart[item]
                amount = quantity * variant.price
                ordered_product = OrderedProduct(quantity=quantity, price=variant.price,
                order=order, product=variant)
                variant.quantity -= quantity
                total+=amount
                variant.save()
                ordered_product.save()
            if voucher:
                if voucher.role == 1:
                    shipping_fee = shipping_fee - voucher.offset
                elif voucher.role == 2:
                    total = total - (total * voucher.sale)/100
                order.voucher = voucher
            # ch??a c?? api c???a b??n giao h??ng n??n b???n em s??? t??? ?????t ra ng??y nh???n h??ng l?? 3 ng??y sau
            estimated = date.today()+timedelta(days=3)

            # T???o th??ng tin ship h??ng
            ordership = OrderShip(estimated_arrival=estimated, price = shipping_fee, ship=department, order=order)
            ordership.save()
            # C???p nh???t ????n h??ng
            order.amount = total + shipping_fee
            order.ship = shipping_fee
            order.save()
            # Xo?? gi??? h??ng c??
            del request.session['cart']
            return HttpResponseRedirect("/boec/success")
        except:
            return HttpResponseRedirect("/boec/failure")



    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        context["user"] = user
        cart = {}
        cart_items = []
        total = 0
        cities = City.objects.all()
        districts = District.objects.all()
        streets = Street.objects.all()
        departments = ShippingDepartment.objects.all()
        address = ShippingAdress.objects.filter(customer=user)
        if 'cart' not in request.session:
            cart = {}
        else:
            cart = request.session['cart']
        for item in cart:
            variant = VariantOption.objects.get(pk=item)
            quantity = cart[item]
            amount = quantity * variant.price
            setattr(variant, 'quantity', quantity)
            setattr(variant, 'total', amount)
            total += amount
            cart_items.append(variant)
        estimated = date.today()+timedelta(days=3)
        context["cart"] = len(cart)
        context["cart_items"] = cart_items
        context["cities"] = cities
        context["districts"] = districts
        context["streets"] = streets
        context["address"] = address
        context["total"] = total
        context["departments"] = departments
        context["estimated"] = estimated

        return render(request, "boec_core/customer/checkout.html",context)
