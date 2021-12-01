from django.shortcuts import render
from .services import OrderService
from .serializers import OrderSerializer

_SERVICE = OrderService()

def home_order(request):
    return render(request, 'home_order.html')

def update_order_screen(request, id):
    product = _SERVICE.search_order_by_id(id)
    return render(request, 'edit-product.html', context={'product':product})

def save_order(request):
    serializer = OrderSerializer(data=request.POST)

def search_order_by_therm(request):
    therm = request.GET.get('therm')
    orders = _SERVICE.search_orders_by_therm(therm)
    return render(request, 'home_order.html', context={'orders':orders})