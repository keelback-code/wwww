from django.contrib import admin
from .models import Product, Customisation, CustomisationOptions


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'stat',
    )

    ordering = ('sku',)


class CustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'associated_product',
        'variable_name',
    )

    ordering = ('associated_product',)


class CustomisationOptionsAdmin(admin.ModelAdmin):
    list_display = (
        'variable',
    )

    ordering = ('variable',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customisation, CustomisationAdmin)
admin.site.register(CustomisationOptions, CustomisationOptionsAdmin)

