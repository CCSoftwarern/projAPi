# Generated by Django 5.0.1 on 2024-01-14 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_alter_clientes_ck_ativo_alter_clientes_online_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='BAIRRO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='CIDADE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='COMPLEMENTO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ENDERECO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ESTADO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='SENHA',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='STATUS',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='TELEFONE_IMPORTADO',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='TOKEN',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='TP_PESSOA',
            field=models.CharField(max_length=1, null=True),
        ),
    ]