from django.shortcuts import render


def checkout(request):
    """
    Function to retrieve wizard battle blog posts.
    """
    return render(request, 'checkout/checkout.html')
