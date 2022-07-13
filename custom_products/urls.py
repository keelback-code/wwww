from django.urls import path
from . import views

urlpatterns = [
    path('custom_hats/', views.DesignCustomHat.as_view(), name='design_custom_hat'),
]