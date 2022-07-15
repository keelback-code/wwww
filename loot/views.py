from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from standard_products.models import Product
# from custom_products.models import CustomProduct

# Based on Code Institute Boutique Ado project.

def view_loot(request):
    """
    Function that renders the loot page.
    """

    return render(request, 'loot/loot.html')


def standard_add_to_loot(request, item_id):
    """
    Function to add a quantity of the specified product to the bag.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))   # will come from template as string so must convert
    redirect_url = request.POST.get('redirect_url')
    loot = request.session.get('loot', {})  # looks for session and initializes to empty dict if doesn't
    # now that we have dict, can put product in it

    if item_id in list(loot.keys()):
        loot[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {loot[item_id]}')
        print("success")
    else:
        loot[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag.')

    request.session['loot'] = loot # this overwrites variable with the updated version
    print(loot)
    print(item_id)
    return redirect(redirect_url)


def standard_adjust_loot(request, item_id):
    """
    Function to adjust the quantity of products in the bag.
    """

    product = get_object_or_404(Product, pk=item_id)  # this is here so messages can access info
    quantity = int(request.POST.get('quantity'))
    loot = request.session.get('loot', {})

    if quantity > 0:
        loot[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {loot[item_id]}')
    else:
        loot.pop(item_id)
        messages.success(request, f'Removed {product.name} from your loot bag')

    request.session['loot'] = loot
    return redirect(reverse('view_loot'))


def standard_remove_from_loot(request, item_id):
    """
    Function to remove an item from the shopping bag.
    """

    # checks for size first so that just deletes that size, not all products
    try:
        product = get_object_or_404(Product, pk=item_id)
        loot.pop(item_id)
        messages.success(request, f'Removed {product.name} from your loot')

        request.session['loot'] = loot
        # return this instead of redirect
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
