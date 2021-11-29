from django.db import models
import uuid

##teste##


class AddressModel(models.Model):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    street = models.CharField(
        db_column="STREET",
        max_length=50
    )

    number = models.CharField(
        db_column="NUMBER",
        max_length=5
    )

    district = models.CharField(
        db_column="DISTRICT",
        max_length=20
    )

    city = models.CharField(
        db_column="CITY",
        max_length=20
    )

    cep = models.CharField(
        db_column="CEP",
        max_length=10
    )

    complement = models.CharField(
        db_column="COMPLEMENT",
        max_length=150
    )

    def __str__(self) -> str:
        return f"ID: {self.id}; Rua: {self.street}"

    class Meta:
        db_table = 'ADDRESS'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
