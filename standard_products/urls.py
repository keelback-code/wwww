from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('add_standard_product/', views.add_standard_product, name='add_standard_product'),
    # path('edit_standard_product/<int:product_id>/', views.edit_standard_product, name='edit_standard_product'),
    # path('delete_standard_product/<int:product_id>/', views.delete_standard_product, name='delete_standard_product'),
    path('custom_hats/', views.DesignCustomHat.as_view(), name='design_custom_hat'),
    path('final_quote/<int:product_id>/', views.final_quote, name='final_quote'),
]