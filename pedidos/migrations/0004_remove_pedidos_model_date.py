# Generated by Django 4.1.3 on 2023-01-13 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_pedidos_model_codpedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos_model',
            name='date',
        ),
    ]