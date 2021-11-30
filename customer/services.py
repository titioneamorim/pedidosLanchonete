import uuid
from django.db.models import Q, Value
from .models import CustomerModel
from django.db.models import Q, Value


class CustomerServices():

    def search_all_customers(self) -> list[CustomerModel]:
        return CustomerModel.objects.all()

    def search_customer_by_id(self, id) -> CustomerModel:
        return CustomerModel.objects.filter(id=id).first()

    def delete_customer(self, customer_id):
        return CustomerModel.objects.filter(id=customer_id).delete()

    def search_customer_by_therm(self, therm) -> list[CustomerModel]:
        return CustomerModel.objects.filter(Q(name__icontains=therm) | Q(phone__icontains=therm))

    def search_customer_by_phone(self, phone) -> CustomerModel:
        return CustomerModel.objects.filter(phone = phone).first()
    