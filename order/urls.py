from django.urls import path
from .views import *

namespace = 'order'

urlpatterns = [
    path('orders/', home_order, name="home_orders"),
<<<<<<< HEAD
    path('products/edit/<uuid:id>/', update_order_screen, name="edit_orders"),
=======
    path('products/edit/<uuid:id>/', update_order_screen, name="edit_order"),
>>>>>>> 6e20def13dce25cd17aebec6fea9726d7e7a39de
    path('products/save', save_order, name="save_order"),
    path('products/search/', search_order_by_therm, name="search_orders"),
]