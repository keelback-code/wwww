from django.shortcuts import render


def privacy_policy(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'operations/privacy_policy.html')
