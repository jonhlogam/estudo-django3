# Generated by Django 4.1.3 on 2023-01-14 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0012_alter_pedidos_model_codpedido'),
        ('pedidos_item', '0005_alter_item_pedidos_codpedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_pedidos',
            name='codpedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos_model'),
        ),
    ]