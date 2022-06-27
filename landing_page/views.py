from django.shortcuts import render


def landing_page(request):
    """
    Function to retrieve the landing page.
    """
    return render(request, 'landing_page/index.html')
