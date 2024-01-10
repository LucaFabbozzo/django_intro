from django.contrib import admin
from .models import Category, Product

# Register your models here.
#configuriamo l'admin per far apparire il nostro modello nel pannello di amministrazione
admin.site.register(Category)
admin.site.register(Product)
