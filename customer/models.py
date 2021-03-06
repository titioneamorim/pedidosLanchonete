from django.db import models
import uuid

from address.models import AddressModel


class CustomerModel(models.Model):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    name = models.CharField(
        db_column="NAME",
        max_length=100
    )

    phone = models.CharField(
        db_column="PHONE",
        max_length=16,
        unique=True,
    )

    address = models.ManyToManyField(AddressModel, related_name='customer')

    def __str__(self) -> str:
        return f"ID: {self.id}; Cliente: {self.name};"

    class Meta:
        db_table = 'CUSTOMER'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

