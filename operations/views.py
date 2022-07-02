from django.shortcuts import render


def ts_and_cs(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'operations/terms_and_conditions.html')
