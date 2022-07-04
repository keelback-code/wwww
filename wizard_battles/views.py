from django.shortcuts import render, get_object_or_404, redirect
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


def view_battle(request):
    """
    Function to retrieve individual wizard battle blog posts.
    """
    return render(request, 'wizard_battles/wizard_battle.html')


# def create_battle(request):
class CreateBattle(generic.CreateView):
    """
    Function to create wizard battle blog posts.
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "wizard_battles/create_battle.html",
            {
                "post_form": PostForm()
            }
        )

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            write_post = post_form.save(commit=False)
            write_post.creator = request.user
            write_post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('landing_page')
        else:
            messages.error(request, 'Post not saved, please try again.')
            post_form = PostForm()

        return render(
            request,
            "wizard_battles/create_battle.html",
            {
                "post_form": post_form,
            }
        )
    # return render(request, 'wizard_battles/create_battle.html')