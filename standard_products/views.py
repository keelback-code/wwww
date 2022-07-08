from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import StandardProduct, Category
from .forms import StandardProductForm


def all_products(request):
    """
    Function to retrieve all products. Based on Code Institute Boutique Ado project.
    """
    products = StandardProduct.objects.all()

    # set query to None so there's no error when page is loaded without a search term
    query = None
    categories = None
    sort = None
    direction = None  # this is for direction of sorting

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'  # to allow for lower case
                products = products.annotate(lower_name=Lower('name'))  # to allow for lower case
            if sortkey == 'category':
                sortkey = 'category__name'  # double underscore allows us to drill into a related model
            if sortkey == 'stat':
                sortkey = 'stat__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # this adds a minus in front of the sortkey to reverse the order
            products = products.order_by(sortkey)  # this is actually sorting it


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        # if 'stat' in request.GET:
        #     stats = request.GET['stat'].split(',')
        #     products = products.filter(stats__name__in=stats)
        #     stats = Stats.objects.filter(name__in=stats)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't entered any search criteria.")
                return redirect(reverse('all_products'))

            # searching name and description for query
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'  # to pass the sort and dir into the html eg price_asc

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'standard_products/products.html', context)


def product_detail(request, product_id):
    """
    Function to retrieve the details of an individual product.
    """
    product = get_object_or_404(StandardProduct, pk=product_id)

    context = {
        'product': product,
        # 'search_term': query,
    }

    return render(request, 'standard_products/product_detail.html', context)


@login_required
def add_standard_product(request):
    """
    Function to add a standard product.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))

    if request.method == 'POST':
        form = StandardProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully saved!')
            return redirect(reverse('all_products'))
        else:
            messages.error(request, 'Product was not added. Please try again.')
    else:
        form = StandardProductForm()

    template = 'standard_products/add_standard_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_standard_product(request, product_id):
    """
    Function to retrieve a standard product for editing.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))

    product = get_object_or_404(StandardProduct, pk=product_id)
    if request.method == 'POST':
        form = StandardProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():  
            product = form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('all_products'))
        else:
            messages.error(request, 'Product was not updated. Please try again.')
    else:
        form = StandardProductForm(instance=product)

    template = 'standard_products/edit_standard_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_standard_product(request, product_id):
    """
    Function to delete standard products.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Apologies, only staff can complete this action.')
        return redirect(reverse('landing_page'))
    
    product = get_object_or_404(StandardProduct, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('all_products'))
