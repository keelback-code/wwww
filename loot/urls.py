from django.urls import path
from . import views

# Based on Code Institute Boutique Ado project.

# urlpatterns = [
#     path('view_loot/', views.view_loot, name='view_loot'),
# ]

urlpatterns = [
    path('', views.view_loot, name='view_loot'),
    path('add/<item_id>/', views.add_to_loot, name='add_to_loot'),
    path('adjust/<item_id>/', views.adjust_loot, name='adjust_loot'),
    path('remove/<item_id>/', views.remove_from_loot, name='remove_from_loot'),
]