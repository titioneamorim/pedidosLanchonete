from django.shortcuts import render
from .services import OrderService
from .serializers import OrderSerializer
from customer.services import CustomerServices
from customer.serializers import CustomerReadSerializer
from product.service import ProductService
from django.core.paginator import Paginator

_SERVICE = OrderService()
__CUSTOMER_SERVICE = CustomerServices()
__PRODUCT_SERVICE = ProductService

def home_order(request):
    return render(request, 'home_order.html')

def create_order(request):
    products = __PRODUCT_SERVICE.search_all_products()
    return render(request, 'create_order.html', context={'products':products})

def update_order_screen(request, id):
    order = _SERVICE.search_order_by_id(id)
    return render(request, 'edit_order.html', context={'order':order})

def save_order(request):
    serializer = OrderSerializer(data=request.POST)

def search_customer_by_phone(request):
    phone = request.GET.get('therm')
    customer = __CUSTOMER_SERVICE.search_customer_by_phone(phone)
    serializer = CustomerReadSerializer(instance=customer)
    return render(request, 'create_order.html', context={'customer':serializer.data})

def create_new_order(request):

    return render(request, 'create_order.html')