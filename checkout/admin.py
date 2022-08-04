from django.contrib import admin
from .models import Order, OrderLineItem
"""
Classes to see checkout objects in the admin,
based on Code Institute's Boutique Ado walkthrough.
"""


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_loot', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total', 'original_loot',
              'stripe_pid', 'fulfilled',)

    list_display = ('order_number', 'date', 'full_name',
                    'fulfilled', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
