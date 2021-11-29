from django.db import models
import uuid

class ProductModel(models.Model):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    name = models.CharField(
        db_column="NAME",
        max_length=100,
    )

    price = models.DecimalField(
        db_column="PRICE",
        max_digits=8,
        decimal_places=2,
    )

    def __str__(self) -> str:
        return f"Id: {self.id}; Produto: {self.name}; Preço: {self.price};"

    class Meta:
        db_table = 'PRODUCT'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        