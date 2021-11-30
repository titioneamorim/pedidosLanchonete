from django.urls import path
from .views import *

namespace = 'order'

urlpatterns = [
    path('orders/', home_order, name="home_orders"),

]