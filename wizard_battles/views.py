from django.shortcuts import render


def view_battle(request):
    """
    Function to retrieve wizard battle blog posts.
    """
    return render(request, 'wizard_battles/battle.html')