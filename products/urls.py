from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('custom_hat_one/', views.DesignCustomHat.as_view(), name='custom_hat_one'),
    path('custom_hat_two/', views.DesignCustomHatTwo.as_view(), name='custom_hat_two'),
    path('custom_cloak/', views.DesignCustomCloak.as_view(), name='custom_cloak'),
    path('custom_wand/', views.DesignCustomWand.as_view(), name='custom_wand'),
    path('final_quote/<int:product_id>/', views.final_quote, name='final_quote'),
    path('staff_path_one/', views.StaffAddProduct.as_view(), name='staff_path_one'),
    path('staff_path_two/', views.StaffCustomise.as_view(), name='staff_path_two'),
    path('staff_path_three/', views.StaffAddOptions.as_view(), name='staff_path_three'),
    path('staff_final/<int:product_id>/', views.staff_final, name='staff_final'),
]