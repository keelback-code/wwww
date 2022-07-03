from django.shortcuts import render


def battle_arena(request):
    """
    Function to retrieve a view of all wizard battle blog posts.
    """
    return render(request, 'wizard_battles/battle_arena.html')


def view_battle(request):
    """
    Function to retrieve individual wizard battle blog posts.
    """
    return render(request, 'wizard_battles/wizard_battle.html')