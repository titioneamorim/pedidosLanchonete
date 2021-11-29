from django.db import models
from django.db.models import fields
from rest_framework.utils import field_mapping
from .models import CustomerModel
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ('__all__')