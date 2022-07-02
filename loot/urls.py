from django.urls import path
from . import views

urlpatterns = [
    path('view_loot/', views.view_loot, name='view_loot'),
]