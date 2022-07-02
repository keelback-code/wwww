from django.shortcuts import render


def view_loot(request):
    """
    Function to retrieve the loot (shopping bag) page.
    """
    return render(request, 'loot/view_loot.html')