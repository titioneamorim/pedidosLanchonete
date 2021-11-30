import uuid
from .models import AddressModel


class AddressServices():

    def save_address(self, request):
        endereco = {
            "street":request.POST.get("street"),
            "number":request.POST.get("number"),
            "district":request.POST.get("district"),
            "city":request.POST.get("city"),
            "cep":(request.POST.get("cep")),
            "complement":request.POST.get("complement"),
        }
        endereco.save()

    def search_address_by_id(self, id_customer:uuid) -> AddressModel:
        return AddressModel.objects.filter(customer__id=id_customer).first()
