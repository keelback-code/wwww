from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('custom_hat_one/', views.DesignCustomHat.as_view(), name='custom_hat_one'),
    path('custom_hat_two/', views.DesignCustomHatTwo.as_view(), name='custom_hat_two'),
    path('custom_cloak/', views.DesignCustomCloak.as_view(), name='custom_cloak'),
    path('custom_wand/', views.DesignCustomWand.as_view(), name='custom_wand'),
    path('custom_sunglasses/', views.DesignCustomSunglasses.as_view(), name='custom_sunglasses'),
    path('custom_spell_book/', views.DesignCustomSpellBook.as_view(), name='custom_spell_book'),
    path('final_quote/<int:product_id>/', views.final_quote, name='final_quote'),
    path('staff_submission/', views.StaffSubmitView.as_view(), name='staff_submission'),
]