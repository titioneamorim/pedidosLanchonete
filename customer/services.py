import uuid
from django.db.models import Q, Value
from .serializers import CustomerSerializer
from .models import CustomerModel


class CustomerServices():
    
    def salvar_customer(self, customer:CustomerSerializer):
        customer.save()
    
    def search_all_customers(self) -> list[CustomerModel]:
        return CustomerModel.objects.all()
    
    def search_customer_by_id(self, id) -> CustomerModel:
        return CustomerModel.objects.filter(id=id).first()
    
    def delete_customer(self, customer_id):
        return CustomerModel.objects.filter(id=customer_id).delete()
    
    
        