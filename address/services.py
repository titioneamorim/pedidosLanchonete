import uuid
from .models import ProductModel

def save_address(request):
    endereco = {
        "street":request.POST.get("street"),
        "number":request.POST.get("number"),
        "district":request.POST.get("district"),
        "city":request.POST.get("city"),
        "cep":(request.POST.get("cep")),
        "complement":request.POST.get("complement"),
    }
    endereco.save()