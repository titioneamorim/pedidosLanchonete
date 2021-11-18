from django.db import models
import uuid

from order.models import OrderModel


class PaymentModel(models.Model):
    id = models.UUIDField(
        db_column="ID",
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    type = models.CharField(
        db_column="TYPE",
        max_length=20,
    )

    order = models.ForeignKey(
        OrderModel,
        db_column="ORDER_ID",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"ID: {self.id}; Tipo: {self.type}"

    class Meta:
        db_table = 'PAYMENT'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
