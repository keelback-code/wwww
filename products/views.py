from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views import generic, View
from .models import Product
from .forms import HatOneForm, HatTwoForm


def calc_variables(variable_one, variable_two, variable_three):
    """
    Function to calculate the variables for each custom product.
    """
    price = 20

    if variable_one == 'A':
        price = price + 5
    elif variable_one == 'B':
        price = price + 10
    elif variable_one == 'C':
        price = price + 15
    else:
        price + 0
    print(price)

    if variable_two == 'A':
        price = price + 5
    elif variable_two == 'B':
        price = price + 10
    elif variable_two == 'C':
        price = price + 15
    else:
        price = price + 0
        
    print(price)

    if variable_three == 'NONE':
        price = price + 0
    else:
        price = price + 2 
    
    print(price)
    return price


def all_products(request):
    """
    Function to retrieve all products.
    """

    return render(request, 'products/products.html')


def product_detail(request, product_id):
    """
    Function to retrieve the details of an individual product.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        # 'search_term': query,
    }

    return render(request, 'products/product_detail.html', context)


class DesignCustomHat(View):
    """
    Function to get a quote for a custom hat.
    """
    def get(self, request):
        form = HatOneForm()
        template = 'products/custom_hat_one.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


    def post(self, request):
        form = HatOneForm(request.POST) 
        brim_width = request.POST['variable_one']
        hat_height = request.POST['variable_two']
        patch = request.POST['variable_three']

        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(brim_width, hat_height, patch)
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request,
                 'Quote was not generated. Width must be at least 5cm and height at least 20cm.\
                 Please try again.')
            form = HatOneForm()

        template = 'products/custom_hat_one.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


class DesignCustomHatTwo(View):
    """
    Function to get a quote for a custom hat.
    """
    def get(self, request):
        form = HatTwoForm()
        template = 'products/custom_hat_two.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


    def post(self, request):
        form = HatTwoForm(request.POST) 
        spell_choices = request.POST['variable_one']
        hat_floppiness = request.POST['variable_two']
        patch = request.POST['variable_three']
        
        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = calc_variables(spell_choices, hat_floppiness, patch)
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request,
                 'Quote was not generated. Width must be at least 5cm and height at least 20cm.\
                 Please try again.')
            form = HatTwoForm()

        template = 'products/custom_hat_two.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


def final_quote(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/final_quote.html', context)

