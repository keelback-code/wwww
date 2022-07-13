from django.urls import path
from . import views

urlpatterns = [
    path('custom_hats/', views.design_custom_hat, name='design_custom_hat'),
]