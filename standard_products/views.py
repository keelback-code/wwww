from django.shortcuts import render


def all_products(request):
    """
    Function to retrieve all products.
    """
    return render(request, 'standard_products/products.html')


def product_detail(request):
    """
    Function to retrieve the details of an individual product.
    """
    return render(request, 'standard_products/product_detail.html')
