import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from .service import ProductService
from .serializers import ProductSerializer
from rest_framework.views import APIView

_SERVICE = ProductService()

def home_products(request, id:uuid=None):
    if id is not None:
        _SERVICE.delete_product_for_id(id)
    elif request.method == "POST" and id is None:
        serializer = ProductSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.data('price').replace[',','.']
            serializer.save()
    products = _SERVICE.search_all_products()
    return render(request, 'home-products.html', context={"products":products})

def edit_product(request, id:uuid):
    product = _SERVICE.search_product_for_id(id)
    
    if request.method == "GET":
        return render(request, 'home-edit-product.html', context={"product":product})

    serializer = ProductSerializer(product, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        serializer.save()
        messages.success(request, "Produto salvo com sucesso")
    return render(request, 'home-edit-product.html', context={"product":product})

def save_product(request, id:uuid):
    serializer = ProductSerializer(data=request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        serializer.data('price').replace[',','.']
        serializer.save()
    products = _SERVICE.search_all_products()
    return render(request, 'home-products.html', context={"products":products})

class ProductSearchView(APIView):
    def get(self, request):
        term = request.GET.get('term')
        products = _SERVICE.search_products_by_term(term)
        return render(request, 'home-products.html', context={'products': products})

