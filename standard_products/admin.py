from django.contrib import admin
from .models import StandardProduct, Stat


class StandardProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'stat',
        'price',
    )

    ordering = ('name',)


class StatAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(StandardProduct, StandardProductAdmin)
admin.site.register(Stat, StatAdmin)
