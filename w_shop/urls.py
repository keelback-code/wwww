from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import handler404, handler500, handler403, handler405


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('operations.urls')),
    path('products/', include('products.urls')),
    path('checkout/', include('checkout.urls')),
    path('loot/', include('loot.urls')),
    path('profiles/', include('profiles.urls')),
    path('wizard_battles/', include('wizard_battles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'w_shop.views.handler404'
handler500 = 'w_shop.views.handler500'
handler403 = 'w_shop.views.handler403'
handler405 = 'w_shop.views.handler405'
