from django.db import models
import uuid

from django.db.models.fields.related import ForeignKey
from address.models import AddressModel
from customer.models import CustomerModel
from product.models import ProductModel
from django_extensions.db.models import TimeStampedModel


class OrderModel(TimeStampedModel):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    order_date = models.DateField(
        db_column='ORDER_DATE',
        auto_now_add=True,
    )

    customer= models.ForeignKey(
        CustomerModel,
        db_column="CUSTOMER_ID",
        on_delete=models.DO_NOTHING,
    )

    address = models.ForeignKey(
        AddressModel,
        db_column="ADDRESS_ID",
        on_delete=models.DO_NOTHING,
    )

    product = models.ForeignKey(
        ProductModel,
        db_column="PRODUCT_ID",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self) -> str:
        return f"ID: {self.id}; Cliente: {self.customer};"

    class Meta:
        db_table = 'ORDER'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'