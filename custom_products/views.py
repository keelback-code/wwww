from django.shortcuts import render
from .models import CustomProduct
from .forms import CustomProductForm


def design_custom_hat(request):
    """
    Function to retrieve the page to get a quote for a custom hat.
    """
    context = {
        "form": CustomProductForm()
    }
    return render(request, 'custom_products/custom_hats.html', context)
