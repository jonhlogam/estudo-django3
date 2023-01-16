# Generated by Django 4.1.3 on 2023-01-16 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_item', '0012_remove_itempedidos_codpedido'),
        ('pedidos', '0014_rename_valortotal_pedidos_model_valor_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos_model',
            old_name='valor_total',
            new_name='valortotal',
        ),
        migrations.AddField(
            model_name='pedidos_model',
            name='itemvalor',
            field=models.ManyToManyField(related_name='item', to='pedidos_item.itempedidos'),
        ),
    ]
