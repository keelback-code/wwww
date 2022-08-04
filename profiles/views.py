from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.views import View
from checkout.models import Order
from checkout.forms import FulfillmentForm
from products.models import StaffSubmission
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile, based on
    Code Institute's Boutique Ado walkthrough.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the user's individual orders.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@staff_member_required
def staff_profile(request):
    """
    Display all orders placed on the site for the Staff Hub.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this page.')
        return redirect(reverse('landing_page'))
    else:
        orders = Order.objects.all()
        staff_products = StaffSubmission.objects.all()

    template = 'profiles/staff_profile.html'
    context = {
        'orders': orders,
        'staff_products': staff_products,
    }

    return render(request, template, context)


@staff_member_required
def staff_order_history(request, order_number):
    """
    Display a user's individual orders and
    allow staff to change its' fulfillment status.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))
    else:
        order = get_object_or_404(Order, order_number=order_number)
        if request.method == 'POST':
            form = FulfillmentForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                messages.success(request, 'Order status successfully updated!')
                return redirect(reverse('staff_profile'))
            else:
                messages.error(request,
                               'Status was not updated. Please try again.')
        else:
            form = FulfillmentForm(instance=order)

        template = 'profiles/staff_order_history.html'
        context = {
            'order': order,
            'form': form,
            'from_profile': True,
        }

    return render(request, template, context)
