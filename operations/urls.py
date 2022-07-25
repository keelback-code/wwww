from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('about_us/', views.about_us, name='about_us'),
    path('delivery_and_questions/', views.delivery_and_questions, name='delivery_and_questions'),
]