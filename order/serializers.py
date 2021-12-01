from .models import OrderModel
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('__all__')