from django.urls import path

from customer.views import customer_home, delete_customer, save_customer, update_customer, update_customer_screen

namespace = 'clientes'

urlpatterns = [
    path('clientes/', customer_home, name="home_clientes"),
    path('clientes/salvar/', save_customer, name="save_customer"),
    path('clientes/altera/<uuid:id>/', update_customer, name="update_customer"),
    path('clientes/alterar/<uuid:id>/', update_customer_screen, name="edit_customer"),
    path('clientes/<uuid:id>/', delete_customer, name="remove_customer"),
    # path('produtos/', home_produtos, name="home_produtos"),
    # path('produtos/busca/', busca_produto, name="consulta_produtos"),
    # path('produtos/adicionar', tela_adicao_produto, name="tela_adiciona_produto"),
    # path('produtos/alterar/<uuid:id>/', tela_edicao_produto, name="edicao_produto"),
    # path('editaprodutos/<uuid:id>/', edita_produto, name="edita_produto"),
    # path('entradasaida/', entrada_saida, name="home_entradasaida"),
]