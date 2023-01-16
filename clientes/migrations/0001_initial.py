# Generated by Django 4.1.3 on 2023-01-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nome', models.TextField(default=None, max_length=100)),
                ('cnpj', models.TextField(default=None, max_length=140, primary_key=True, serialize=False)),
                ('senha', models.TextField(default=None, max_length=120)),
                ('email', models.TextField(default=None, max_length=120)),
                ('telefone', models.TextField(default=None, max_length=120)),
                ('confirma_senha', models.TextField(default=None, max_length=120)),
                ('status', models.BooleanField(default=False)),
                ('codtabela', models.IntegerField(default=0)),
            ],
        ),
    ]
