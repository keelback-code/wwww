from django.shortcuts import render


def custom_hats(request):
    """
    Function to retrieve the page to get a quote for a custom hat.
    """
    return render(request, 'custom_products/custom_hats.html')
