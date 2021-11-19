import uuid
from .models import ProductModel
from django.db.models import Q

class ProductService():

    def search_all_products(self) -> list[ProductModel]:
        return ProductModel.objects.all()

    #def search_product_for_id(self, id:uuid) -> ProductModel:
    #    return ProductModel.objects.filter(id=id).first()
    
    #def search_product_for_code(self, code:str) -> ProductModel:
    #    return ProductModel.objects.filter(code=code).first()
    
    def delete_product_for_id(self, id:uuid) -> int:
        return ProductModel.objects.filter(id=id).delete()

    #def search_products_by_term(self, term:str):
    #    return ProductModel.objects.annotate().filter(Q(name__icontains=term) | Q(price__icontains=term)).order_by('name')