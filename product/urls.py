from django.urls import path
from .views import *

namespace = 'product'

urlpatterns = [
    path('products/', product_home, name="home_products"),
    path('products/<uuid:id>/', delete_product, name="delete_products"),
    path('products/edit/<uuid:id>/', update_product_screen, name="edit_product"),
    path('products/save', save_product, name="save_product"),
    path('products/search/', search_product_by_therm, name="search_product"),
    path('products/editar/<uuid:id>/', update_product, name="update_product"),
]