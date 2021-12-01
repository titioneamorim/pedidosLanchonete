import uuid
from django.shortcuts import render
from django.contrib import messages

from product.models import ProductModel
from .service import ProductService
from .serializers import ProductSerializer
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator
import locale



_SERVICE = ProductService()

def product_home(request):
    products = _SERVICE.search_all_products()
    page = request.GET.get('p')
    paginator = Paginator(products, 5)
    products = paginator.get_page(page)
    return render(request, 'home-products.html', context={'products':products})

def delete_product(request, id):
    _SERVICE.delete_product_for_id(id)
    messages.success(request,"Produto removido com sucesso!")
    return HttpResponseRedirect('/products/') 

def update_product_screen(request, id):
    product = _SERVICE.search_product_by_id(id)
    return render(request, 'edit-product.html', context={'product':product})

def save_product(request):
    serializer = ProductSerializer(data=request.POST)

    if not serializer.is_valid():
        messages.warning(request, "Erro ao cadastrar produto")
        return HttpResponseRedirect('/products/')        
    serializer.save()
    messages.success(request,"Produto "+ request.POST.get('name') +" salvo com sucesso.")
    return HttpResponseRedirect('/products/')  

def search_product_by_therm(request):
    therm = request.GET.get('therm')
    products = _SERVICE.search_products_by_therm(therm)
    return render(request, 'home-products.html', context={'products':products})

def add_product_screen(request):
    return render(request, 'product-add.html')

def update_product(request, id:uuid):
    product = _SERVICE.search_product_by_id(id)
    serializer = ProductSerializer(product, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer)
    else:
        serializer.save()
        messages.success(request, "Produto "+ request.POST.get('name') +" alterado com sucesso")    
    return HttpResponseRedirect('/products/')


