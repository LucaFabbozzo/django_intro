# Generated by Django 4.1.7 on 2024-01-10 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]