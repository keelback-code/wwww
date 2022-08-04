from django.shortcuts import render


def landing_page(request):
    """
    Function to retrieve the landing page.
    """
    return render(request, 'operations/index.html')


def privacy_policy(request):
    """
    Function to retrieve the privacy policy page.
    """
    return render(request, 'operations/privacy_policy.html')


def about_us(request):
    """
    Function to retrieve the about us page.
    """
    return render(request, 'operations/about_us.html')


def delivery_and_questions(request):
    """
    Function to retrieve the FAQ page.
    """
    return render(request, 'operations/delivery_and_questions.html')
