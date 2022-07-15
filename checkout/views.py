from django.shortcuts import render


def checkout(request):
    """
    Function to retrieve the checkout page.
    """
    return render(request, 'checkout/checkout.html')
