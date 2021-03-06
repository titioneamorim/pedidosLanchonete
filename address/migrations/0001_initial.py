# Generated by Django 3.2.9 on 2021-11-30 23:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('street', models.CharField(db_column='STREET', max_length=50)),
                ('number', models.CharField(db_column='NUMBER', max_length=5)),
                ('district', models.CharField(db_column='DISTRICT', max_length=20)),
                ('city', models.CharField(db_column='CITY', max_length=20)),
                ('cep', models.CharField(db_column='CEP', max_length=10)),
                ('complement', models.CharField(blank=True, db_column='COMPLEMENT', max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'db_table': 'ADDRESS',
            },
        ),
    ]
