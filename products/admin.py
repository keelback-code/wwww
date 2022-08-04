from django.contrib import admin
from .models import Product, StaffSubmission


class ProductAdmin(admin.ModelAdmin):
    """
    Class for seeing products in the Django Admin.
    """
    list_display = (
        'product_type',
        'stat',
    )

    ordering = ('product_type',)


class StaffSubmissionAdmin(admin.ModelAdmin):
    """
    Class for seeing staff submissions in the Django Admin.
    """
    list_display = (
        'staff_member',
        'product_type',
        'created_on',
    )

    ordering = ('created_on',)


admin.site.register(Product, ProductAdmin)
admin.site.register(StaffSubmission, StaffSubmissionAdmin)
