from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    exclude = ('create_at', )
    list_display = ('id', 'name', 'stock', 'create_at')

# Register your models here.
#configuriamo l'admin per far apparire il nostro modello nel pannello di amministrazione
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
