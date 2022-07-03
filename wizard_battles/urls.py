from django.urls import path
from . import views

urlpatterns = [
    path('wizard_battle/', views.view_battle, name='view_battle'),  # change to <slug:wizard_battle>/
    path('battle_arena/', views.battle_arena, name='battle_arena'),
    # path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
