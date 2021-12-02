import uuid
from .models import OrderModel
from django.db.models import Q
from .serializers import OrderSerializer
from product.models import ProductModel

class OrderService():

    def search_all_orders(self) -> list[OrderModel]:
        return OrderModel.objects.all()

    def search_order_by_id(self, id) -> OrderModel:
        return OrderModel.objects.filter(id=id).first()

    def save_order(self, product: OrderSerializer):
        product.save()

    def search_customer_by_phone(self, phone) -> OrderModel:
        return OrderModel.objects.filter(customer__phone__icontains=phone).first()