from django.contrib import admin
from .models import StandardProduct, Category


class StandardProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(StandardProduct, StandardProductAdmin)
admin.site.register(Category, CategoryAdmin)
