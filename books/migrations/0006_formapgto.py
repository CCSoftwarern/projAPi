# Generated by Django 4.2.2 on 2023-06-27 02:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPgto',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DESCRICAO', models.CharField(max_length=100)),
                ('STATUS', models.CharField(default='0', max_length=1)),
                ('ID_EMPRESA', models.IntegerField(default=0)),
            ],
        ),
    ]
