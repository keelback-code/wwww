from django.shortcuts import render, redirect, reverse, \
                             HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_loot(request):
    """
    Function that renders the loot page.
    """
    return render(request, 'loot/loot.html')


def add_to_loot(request, item_id):
    """
    Function to add a quantity of the specified product to the bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    loot = request.session.get('loot', {})

    if item_id in list(loot.keys()):
        loot[item_id] += quantity
        messages.success(request,
                         f'Updated custom product quantity to {loot[item_id]}')
    else:
        loot[item_id] = quantity
        messages.success(request, 'Added custom product to your loot')

    request.session['loot'] = loot
    return redirect(redirect_url)


def adjust_loot(request, item_id):
    """
    Function to adjust the quantity of products in the bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    loot = request.session.get('loot', {})

    if quantity <= 10:
        loot[item_id] = quantity
        messages.success(request,
                         f'Updated custom product quantity to {loot[item_id]}')
    elif quantity > 10:
        messages.error(request, 'Unable to add more than 10 custom products')
    else:
        loot.pop(item_id)
        messages.success(request, 'Removed custom product from your loot')

    request.session['loot'] = loot
    return redirect(reverse('view_loot'))


def remove_from_loot(request, item_id):
    """
    Function to remove an item from the shopping bag.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        loot = request.session.get('loot', {})
        loot.pop(item_id)
        messages.success(request, 'Removed custom product from your loot')
        product.delete()

        request.session['loot'] = loot
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
