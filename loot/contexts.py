
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from products.models import Product


def loot_contents(request):
    """
    Function to make loot bag available across the site;
    based on Code Institute's Boutique Ado code walkthrough.
    """
    loot_items = []
    total = 0
    product_count = 0
    loot = request.session.get('loot', {})

    for item_id, item_data in loot.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            loot_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total
    
    context = {
        'loot_items': loot_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
