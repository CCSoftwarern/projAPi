# Generated by Django 5.0.1 on 2024-01-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0036_alter_motoboys_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motoboys',
            old_name='ID',
            new_name='ID_MOTOBOY',
        ),
    ]