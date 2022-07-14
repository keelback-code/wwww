from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.views import generic, View

from .models import CustomProduct
from .forms import CustomProductForm


class DesignCustomHat(View):
    """
    Function to get a quote for a custom hat.
    """
    def get(self, request):
        form = CustomProductForm()
        template = 'custom_products/custom_hats.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


    def post(self, request):
        form = CustomProductForm(request.POST) 
        brim_width = request.POST['brim_width']
        hat_height = request.POST['hat_height']
        patch = request.POST['patch']
        brim = int(brim_width)
        height = int(hat_height)
        price = 20

        if brim <= 10:
            price = price + 5
        elif brim <= 15:
            price = price + 10
        elif brim <= 20:
            price = price + 15
        else:
            price + 0
        
        if height <= 25:
            price = price + 5
        elif height <= 30:
            price = price + 10
        elif height <= 35:
            price = price + 15
        else:
            price = price + 0

        if patch == 'NONE':
            price = price + 0
        else:
            price = price + 2 

        if form.is_valid():
            priced_form = form.save(commit=False)
            priced_form.price = price
            product = form.save()
            return redirect(reverse('final_quote', args=[product.id]))
        else:
            messages.error(request,
                 'Quote was not generated. Width must be at least 5cm and height at least 20cm.\
                 Please try again.')
            form = CustomProductForm()

        template = 'custom_products/custom_hats.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


def final_quote(request, product_id):
    
    product = get_object_or_404(CustomProduct, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'custom_products/final_quote.html', context)
