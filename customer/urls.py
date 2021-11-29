from django.urls import path

from customer.views import customer_home, delete_customer, save_customer, search_customer_by_therm, update_customer, update_customer_screen

namespace = 'clientes'

urlpatterns = [
    path('clientes/', customer_home, name="home_clientes"),
    path('clientes/salvar/', save_customer, name="save_customer"),
    path('clientes/altera/<uuid:id>/', update_customer, name="update_customer"),
    path('clientes/alterar/<uuid:id>/', update_customer_screen, name="edit_customer"),
    path('clientes/<uuid:id>/', delete_customer, name="remove_customer"),
    path('clientes/busca/', search_customer_by_therm, name="search_customer"),
]
