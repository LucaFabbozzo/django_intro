# Generated by Django 4.1.7 on 2024-01-10 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_creado_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='creado_en',
            new_name='create_at',
        ),
    ]
