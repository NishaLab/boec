from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import logging

@csrf_exempt
def add_product_to_cart(request):
  key = request.POST.get('id') + ""
  quant = request.POST.get('quantity')
  quant = int(quant)
  if quant is None:
    quant = 1
  is_new = False
  if 'cart' not in request.session:
    cart = {
      key: quant
    }
    is_new = True
    request.session['cart']= cart
  else:
    cart = request.session['cart']
    if (key) in cart:
      cart[key] += quant
    else:
      cart[key]  = quant
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

@csrf_exempt
def add_review(request):
  product = ProductVariant.objects.get(pk=request.POST.get('id'))
  user = User.objects.get(pk=request.POST.get('user'))
  rating = int(request.POST.get('rating'))
  comment = request.POST.get('comment')
  review = CustomerReview(customer= user, product=product, rating= rating, content= comment)
  review.save()
  return JsonResponse({
      "msg": "Success",
  })

@csrf_exempt
def add_reply(request):
  review = CustomerReview.objects.get(pk=request.POST.get('id'))
  user = User.objects.get(pk=request.POST.get('user'))
  comment = request.POST.get('content')
  reply = Reply(staff= user, review=review, content= comment)
  reply.save()
  return JsonResponse({
      "msg": "Success",
  })