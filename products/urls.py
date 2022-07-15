from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('custom_hat_one/', views.DesignCustomHat.as_view(), name='custom_hat_one'),
    path('custom_hat_two/', views.DesignCustomHatTwo.as_view(), name='custom_hat_two'),
    path('final_quote/<int:product_id>/', views.final_quote, name='final_quote'),
]