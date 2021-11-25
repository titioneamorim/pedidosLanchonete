from django.urls import path
from .views import *

namespace = 'product'

urlpatterns = [
    path('products/', home_products, name="home_products"),
    path('products/<uuid:id>/', home_products, name="delete_products"),
    path('products/edit/<uuid:id>/', edit_product, name="home_edit_product"),
    path('products/save', save_product, name="save_product"),
    #path('search/', ProductSearchView.as_view(), name='search'),
]