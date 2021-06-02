from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import logging

@csrf_exempt
def add_product_to_cart(request):
  key = request.POST.get('id') + ""
  is_new = False
  if 'cart' not in request.session:
    cart = {
      key: 1
    }
    is_new = True
    request.session['cart']= cart
  else:
    cart = request.session['cart']
    if (key) in cart:
      cart[key] += 1
    else:
      cart[key]  = 1
      is_new = True
    request.session['cart']= cart
  return JsonResponse({
      "msg": "Success",
      "cart": cart,
      "is_new": is_new,
  })
@csrf_exempt
def add_product_to_favorite(request):
  product = ProductVariant.objects.get(pk=request.POST.get('id'))
  user = User.objects.get(pk=request.POST.get('user'))
  try:
    fav = Favorite.objects.get(product=product,customer=user)
    is_exist = True
    fav.delete()
  except:
    is_exist = False
    fav = Favorite(product=product,customer=user)
    fav.save()


  return JsonResponse({
      "msg": "Success",
      "is_exist": is_exist,
  })