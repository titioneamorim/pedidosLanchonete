from django.shortcuts import render
from .services import OrderService
from .serializers import OrderSerializer
from customer.services import CustomerServices
from address.services import AddressServices

_SERVICE = OrderService()
__CUSTOMER_SERVICE = CustomerServices()
__ADDRESS_SERVICE = AddressServices

def home_order(request):
    return render(request, 'home_order.html')

def create_order(request):
    return render(request, 'create_order.html')

def update_order_screen(request, id):
    order = _SERVICE.search_order_by_id(id)
    return render(request, 'edit_order.html', context={'order':order})

def save_order(request):
    serializer = OrderSerializer(data=request.POST)

def search_customer_by_phone(request):
    phone = request.GET.get('therm')
    customer = __CUSTOMER_SERVICE.search_customer_by_phone(phone)
    address = __ADDRESS_SERVICE.search_address_by_id(customer.id)
    return render(request, 'create_order.html', context={'customer':customer, 'address':address})

def create_new_order(request):

    return render(request, 'create_order.html')