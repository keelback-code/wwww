from django.shortcuts import render


def privacy_policy(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'operations/privacy_policy.html')


def about_us(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'operations/about_us.html')


def delivery_and_questions(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'operations/delivery_and_questions.html')