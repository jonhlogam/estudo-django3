# Generated by Django 4.1.3 on 2023-01-15 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0013_rename_valor_total_pedidos_model_valortotal'),
        ('pedidos_item', '0008_rename_item_quantidade_item_pedidos_itemquantidade_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item_pedidos',
            new_name='Itempedidos',
        ),
    ]