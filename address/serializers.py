from django.db import models
from django.db.models import fields
from rest_framework.utils import field_mapping
from .models import AddressModel
from rest_framework import serializers

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ('street','number', 'district','city','cep', 'complement',)
    
