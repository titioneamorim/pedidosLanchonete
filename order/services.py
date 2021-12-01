import uuid
from .models import OrderModel
from django.db.models import Q
from .serializers import OrderSerializer

class OrderService():

    def search_all_orders(self) -> list[OrderModel]:
        return OrderModel.objects.all()

    def search_order_by_id(self, id) -> OrderModel:
        return OrderModel.objects.filter(id=id).first()

    def save_order(self, product: OrderSerializer):
        product.save()

    def search_orders_by_therm(self, therm) -> list[OrderModel]:
        return OrderModel.objects.filter(Q(customer__name__icontains=therm) | Q(customer__phone__icontains=therm))