# Generated by Django 5.2 on 2025-05-16 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_sku'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SupplierProduct',
        ),
    ]
