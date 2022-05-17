# Generated by Django 4.0.4 on 2022-05-17 03:43

import core.custom_validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=253)),
                ('value', models.FloatField(validators=[core.custom_validators.validate_interval])),
                ('quantity', models.FloatField(validators=[core.custom_validators.validate_interval])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(validators=[core.custom_validators.validate_interval])),
                ('quantity', models.FloatField(validators=[core.custom_validators.validate_interval])),
                ('requester', models.CharField(max_length=253)),
                ('zip_code', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=253)),
                ('address', models.CharField(max_length=253)),
                ('district', models.CharField(max_length=253)),
                ('number', models.PositiveIntegerField()),
                ('dispatcher', models.CharField(max_length=253)),
                ('situation', models.PositiveIntegerField(validators=[core.custom_validators.validate_interval])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
