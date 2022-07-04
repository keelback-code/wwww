from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic, View
from .models import Post, Comment
from .forms import PostForm, CommentForm


def battle_arena(request):
    """
    Function to retrieve a view of all wizard battle blog posts.
    """
    return render(request, 'wizard_battles/battle_arena.html')


# @login_required  # maybe?
def view_battle(request, slug):
    """
    Function to retrieve individual wizard battle blog posts.
    """
    battle = get_object_or_404(Post, slug=slug)

    context = {
        "battle": battle
    }

    return render(request, 'wizard_battles/wizard_battle.html', context)


@login_required
def create_battle(request):
# class CreateBattle(generic.CreateView):
    """
    Function to create wizard battle blog posts.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            to_save = form.save(commit=False)
            to_save.author = request.user
            to_save.save()
            messages.success(request, 'Wizard Battle successfully started!')
            return redirect(reverse('landing_page'))
        else:
            messages.error(request, 'Wizard Battle aborted. Please try again.')
    else:
        form = PostForm()

    template = 'wizard_battles/create_battle.html'
    context = {
        'form': form,
    }

    return render(request, template, context)