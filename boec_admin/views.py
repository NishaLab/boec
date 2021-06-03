from django.shortcuts import redirect, render
from django.http import HttpResponse
from boec_core.models import *

# Create your views here.
def index(request):
    return render(request,"common/index.html")

def oders(request):
    list_Order = Order.objects.all()
    # list_Amount = []
    # for oder in list_Order:    
    #     list_OrderProduct = OrderedProduct.objects.get(oder = oder.id)
    #     total = 0
    #     for item in list_OrderProduct:
    #         total += item.price
    #     list_Amount.append(total)
    return render(request, "common/oders.html", {"oders":list_Order} )

def detailOrder(request,order_id):
    products = OrderedProduct.objects.get(order = order_id)
    return render(request, 'common/detail_order.html')
    
    oders = [1,2,3,4,5,6]
    return render(request, "common/oders.html", {"oders":oders} )
def productlist(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    return render(request, "common/productlist.html",{'products':products,'categorys':categorys,'sub_categorys':sub_categorys})

def addProduct(request):
    name= request.GET['product_name']
    price = request.GET['price']
    quantity = request.GET['quantity']
    id_ca = request.GET['category']
    id_sub = request.GET['subcategory']
    category = Category.objects.get(id=id_ca)
    sub = SubCategory.objects.get(id=id_sub)
    discription =request.GET['disscription']
    category= Category( name='dien tu', desc='dat')
    category.save()
    Product.objects.create(name=name, desc = discription,category= category,sub_category=sub)
    data = Product.objects.all()
    return redirect('productlist')

def deleteProduct(request,product_id):

    Product.objects.get(id=product_id).delete()
    return redirect('productlist')

def editProduct(request,product_id):
    if request.method == 'POST':
        id = request.POST['id']
        product = Product.objects.get(id=id)
        name = request.POST['name']
        desc = request.POST['description']
        id_category = request.POST['category']
        category = Category.objects.get(id=id_category)
        id_sub = request.POST['subcategory']
        sub = SubCategory.objects.get(id=id_sub)
        product.name = name
        product.desc = desc
        product.category = category
        product.sub_category = sub
        product.save()
        return redirect('productlist')



    product = Product.objects.get(id=product_id)
    categorys = Category.objects.all()
    sub_categorys = SubCategory.objects.all()
    return render(request, "common/productEdit.html",{'product':product,'categorys':categorys,'sub_categorys':sub_categorys})
