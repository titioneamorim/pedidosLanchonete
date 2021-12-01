from django.urls import path
from .views import *

namespace = 'order'

urlpatterns = [
    path('orders/', home_order, name="home_orders"),
    path('orders/create', create_order, name="create_order"),
    path('orders/edit/<uuid:id>/', update_order_screen, name="edit_order"),
    path('orders/save', save_order, name="save_order"),
    path('orders/search/', search_customer_by_phone, name="search_customer_to_order"),
    path('orders/create/', create_new_order, name="create_new_order"),

]