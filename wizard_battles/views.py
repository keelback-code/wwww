from django.shortcuts import render, get_object_or_404, redirect, reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views import generic, View
from .models import Post, Comment
from .forms import PostForm, CommentForm

def test(request):
    """
    Function to retrieve a view of all wizard battle blog posts.
    """


    return render(request, 'wizard_battles/test.html')

def battle_arena(request):
    """
    Function to retrieve a view of all wizard battle blog posts.
    """
    context = {
        "all_battles": Post.objects.all()
    }

    return render(request, 'wizard_battles/battle_arena.html', context)


def view_battle(request, slug):
    """
    Function to retrieve individual wizard battle blog posts.
    """
    battle = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    comments = Comment.objects.filter(post=battle)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            to_save = form.save(commit=False)
            to_save.post = battle
            to_save.save()
            messages.success(request, 'Comment successfully sent by raven!')
            return redirect(reverse('battle_arena'))
        else:
            messages.error(request, 'Your comment was not received by the wizards. Please try again.')
    else:
        form = CommentForm()


    context = {
        'battle': battle,
        'form': form,
        'comments': comments
    }

    return render(request, 'wizard_battles/wizard_battle.html', context)


@staff_member_required
def create_battle(request):
    """
    Function to create wizard battle blog posts.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))
    else:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                to_save = form.save(commit=False)
                to_save.author = request.user
                to_save.save()
                messages.success(request, 'Wizard Battle successfully started!')
                return redirect(reverse('battle_arena'))
            else:
                messages.error(request, 'Wizard Battle attempt abandoned. Please try again.')
        else:
            form = PostForm()

        template = 'wizard_battles/create_battle.html'
        context = {
            'form': form,
        }

    return render(request, template, context)


@staff_member_required
def edit_battle(request, slug):
    """
    Function to retrieve individual wizard battle blog posts for editing.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))
    else:
        battle = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=battle)
            if form.is_valid():
                battle = form.save()
                messages.success(request, 'Wizard Battle successfully updated!')
                return redirect(reverse('battle_arena'))
            else:
                messages.error(request, 'Wizard Battle update attempt abandoned. Please try again.')
        else:
            form = PostForm(instance=battle)

        template = 'wizard_battles/edit_battle.html'
        context = {
            'form': form,
            'battle': battle
        }

    return render(request, template, context)


@staff_member_required
def delete_battle(request, slug):
    """
    Function to delete wizard battle blog posts.
    """
    if not request.user.is_staff:
        messages.error(request, 'Apologies, only staff can access this.')
        return redirect(reverse('landing_page'))
    else:
        battle = get_object_or_404(Post, slug=slug)
        battle.delete()
        messages.success(request, 'Wizard Battle deleted.')
        return redirect(reverse('battle_arena'))
