from django.shortcuts import render


def user_profile(request):
    """
    Function to retrieve the user profile page.
    """
    return render(request, 'profiles/user_profile.html')
