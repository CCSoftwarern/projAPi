# Generated by Django 5.0.1 on 2024-01-14 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0030_alter_formapgto_id_alter_motoboys_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeusLocais',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('ENDERECO', models.CharField(max_length=255, null=True)),
                ('APELIDO_LOCAL', models.CharField(max_length=100, null=True)),
                ('DT_CADASTRO', models.DateTimeField(auto_now_add=True)),
                ('VALOR', models.FloatField(null=True)),
                ('TP', models.CharField(max_length=1, null=True)),
                ('ID_PESSOA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.question')),
            ],
        ),
    ]
