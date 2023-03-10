# Generated by Django 4.1.3 on 2023-01-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_item', '0002_alter_itempedidos_itemvalor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedidos',
            name='id',
        ),
        migrations.AddField(
            model_name='itempedidos',
            name='id_item',
            field=models.TextField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='itemquantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='numseq',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
