# Generated by Django 4.2.2 on 2023-08-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0018_alter_clientes_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes",
            name="SENHA",
            field=models.CharField(default="Não informado", max_length=10),
        ),
        migrations.AlterField(
            model_name="clientes",
            name="STATUS",
            field=models.CharField(default="Não informado", max_length=1),
        ),
    ]
