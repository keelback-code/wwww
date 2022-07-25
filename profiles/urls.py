from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    # path('staff_profile/', views.staff_order_history, name='staff_order_history'),
    path('staff_profile/', views.StaffOrderHistory.as_view(), name='staff_order_history'),
]