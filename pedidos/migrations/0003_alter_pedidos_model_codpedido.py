# Generated by Django 4.1.3 on 2023-01-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_pedidos_model_codpedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos_model',
            name='codpedido',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
