# Generated by Django 5.1.2 on 2024-11-17 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0014_produto_controle_estoque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='preco_de_cursto',
            new_name='preco_de_custo',
        ),
    ]
