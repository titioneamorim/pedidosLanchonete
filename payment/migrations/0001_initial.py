# Generated by Django 3.2.9 on 2021-11-30 23:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(db_column='TYPE', max_length=20)),
                ('order', models.ForeignKey(db_column='ORDER_ID', on_delete=django.db.models.deletion.CASCADE, to='order.ordermodel')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'PAYMENT',
            },
        ),
    ]
