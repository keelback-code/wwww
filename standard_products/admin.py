from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'stat',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)

