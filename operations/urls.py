from django.urls import path
from . import views

urlpatterns = [
    path('terms_and_conditions/', views.ts_and_cs, name='terms_and_conditions'),
]