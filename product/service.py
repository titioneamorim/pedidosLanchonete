import uuid
from .models import ProductModel
from django.db.models import Q
from .serializers import ProductSerializer

class ProductService():

    def delete_product_for_id(self, id:uuid) -> int:
        return ProductModel.objects.filter(id=id).delete()

    def search_all_products(self) -> list[ProductModel]:
        return ProductModel.objects.all()

    def search_product_by_id(self, id) -> ProductModel:
        return ProductModel.objects.filter(id=id).first()

    def salvar_product(self, product: ProductSerializer):
        product.save()

    def search_products_by_therm(self, therm) -> list[ProductModel]:
        return ProductModel.objects.filter(Q(name__icontains=therm) | Q(price__icontains=therm))