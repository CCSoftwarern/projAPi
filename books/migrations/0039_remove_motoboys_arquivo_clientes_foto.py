# Generated by Django 5.0.1 on 2024-01-26 12:39

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0038_motoboys_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motoboys',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='clientes',
            name='FOTO',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.upload_image_clientes),
        ),
    ]