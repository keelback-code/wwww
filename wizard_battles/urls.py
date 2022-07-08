from django.urls import path
from . import views

urlpatterns = [
    path('wizard_battle/<slug:slug>/', views.view_battle, name='view_battle'),  # change to <slug:wizard_battle>/
    path('battle_arena/', views.battle_arena, name='battle_arena'),  # all battles
    path('create_battle/', views.create_battle, name='create_battle'),
    path('edit_battle/<slug:slug>/', views.edit_battle, name='edit_battle'),
]
