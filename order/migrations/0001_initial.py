# Generated by Django 3.2.9 on 2021-11-17 00:50

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_date', models.DateField(auto_now_add=True, db_column='ORDER_DATE')),
                ('address', models.ForeignKey(db_column='ADDRESS_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='address.addressmodel')),
                ('customer', models.ForeignKey(db_column='CUSTOMER_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customermodel')),
                ('product', models.ForeignKey(db_column='PRODUCT_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='product.productmodel')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'ORDER',
            },
        ),
    ]