from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from standard_products.models import StandardProduct


def loot_contents(request):
    """
    Context processor for the shopping bag (loot) functionality.
    Based on Code Institute Boutique Ado project.
    """
    loot_items = []
    total = 0
    product_count = 0
    loot = request.session.get('loot', {})

    for item_id, item_data in loot.items():
        if isinstance(item_data, int):
            product = get_object_or_404(StandardProduct, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            loot_items.append({
                'item_id': item_id,
                'quantity': item_data,  # correct to be item data that was passed in
                'product': product,
            })

    # if total < settings.FREE_DELIVERY_THRESHOLD:
    #     delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    #     free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    # else:
    #     delivery = 0
    #     free_delivery_delta = 0

    # grand_total = delivery + total

    context = {
        'loot_items': loot_items,
        'total': total,
        'product_count': product_count,
        # 'delivery': delivery,
        # 'free_delivery_delta': free_delivery_delta,
        # 'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        # 'grand_total': grand_total,
    }

    return context
