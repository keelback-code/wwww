from django.urls import path
from . import views

urlpatterns = [
    path('custom_hats/', views.custom_hats, name='custom_hats'),
]