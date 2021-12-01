from django.urls import path
from .views import *

namespace = 'order'

urlpatterns = [
    path('orders/', home_order, name="home_orders"),
    path('products/edit/<uuid:id>/', update_order_screen, name="edit_order"),
    path('products/save', save_order, name="save_order"),
    path('products/search/', search_order_by_therm, name="search_orders"),
]