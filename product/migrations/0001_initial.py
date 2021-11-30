# Generated by Django 3.2.9 on 2021-11-30 23:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=100)),
                ('price', models.DecimalField(db_column='PRICE', decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'PRODUCT',
            },
        ),
    ]
