from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic, View

from .models import CustomProduct
from .forms import CustomProductForm


class DesignCustomHat(View):
    """
    Function to get a quote for a custom hat.
    """
    def get(self, request, *args, **kwargs):
        form = CustomProductForm()
        template = 'custom_products/custom_hats.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


    def post(self, request, *args, **kwargs):
        form = CustomProductForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully saved!')
            return redirect(reverse('view_loot'))
        else:
            messages.error(request, 'Product was not added. Please try again.')
            form = CustomProductForm()

        template = 'custom_products/custom_hats.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
