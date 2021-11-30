from django.db import models
from django.db.models import fields
from rest_framework.utils import field_mapping

from address.models import AddressModel
from .models import CustomerModel

from address.serializers import AdressSerializer
from .models import CustomerModel
from rest_framework import serializers

class CustomerReadSerializer(serializers.ModelSerializer):
    address = AdressSerializer(many=True)
    class Meta:
        model = CustomerModel
        fields = ('id', 'name', 'phone', 'address')

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ('id', 'name', 'phone', 'address')