import uuid
from django.http import request
from django.shortcuts import render
from rest_framework import serializers
from django.core.paginator import Paginator
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from address.models import AddressModel
from address.serializers import AdressSerializer
from django.core.paginator import Paginator
import json

from customer.models import CustomerModel
from customer.serializers import CustomerSerializer
from customer.services import CustomerServices


__SERVICE = CustomerServices()


def customer_home(request):
    customers = __SERVICE.search_all_customers()
    page = request.GET.get('p')
    paginator = Paginator(customers, 5)
    customers = paginator.get_page(page)
    return render(request, 'customer.html', context={'customers':customers})

def add_customer_screen(request):
    return render(request, 'add_customer.html')

def save_customer(request):
    data = {
        "street":request.POST.get("street"),
        "number":request.POST.get("number"),
        "district":request.POST.get("district"),
        "city":request.POST.get("city"),
        "cep":(request.POST.get("cep")),
        "complement":request.POST.get("complement"),
    }
    endereco = AdressSerializer(data=data)
    if not endereco.is_valid():
        messages.warning(request, endereco.errors)
        return HttpResponseRedirect('/clientes/')
    endereco.save()
    data_customer = {
        "name":request.POST.get("name"),
        "phone":request.POST.get("phone"),
        "adress":[endereco],
    }
    serializer = CustomerSerializer(data=data_customer)
    if not serializer.is_valid():
        messages.warning(request, serializer.errors, "Erro ao cadastrar cliente")
        return HttpResponseRedirect('/clientes/')
    serializer.save()
    messages.success(request,"Cliente "+ request.POST.get('name') +" salvo com sucesso.")
    return HttpResponseRedirect('/clientes/')        

def update_customer_screen(request, id):
    customer = __SERVICE.search_customer_by_id(id)
    return render(request, 'edit_customer.html', context={'customer':customer})

def delete_customer(request, id):
    __SERVICE.delete_customer(id)
    messages.success(request,"Cliente removido com sucesso.")
    return HttpResponseRedirect('/clientes/')  

def update_customer(request, id:uuid):
    customer = __SERVICE.search_customer_by_id(id)
    serializer = CustomerSerializer(customer, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer)
    else:
        serializer.save()
        messages.success(request, "Cliente "+ request.POST.get('name') +" alterado com sucesso")    
    return HttpResponseRedirect('/clientes/')

def search_customer_by_therm(request):
    therm = request.GET.get('therm')
    customers = __SERVICE.search_customer_by_therm(therm)
    return render(request, 'customer.html', context={'customers':customers})


# def replace(texto:str, sub, oque:str):
#     ["(", ")", "-"]
#     for s in sub:
#         texto.replace(s, oque)