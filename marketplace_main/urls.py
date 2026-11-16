from django.contrib import admin
from django.urls import path
from store.views import home, agregar_al_carrito, ver_carrito
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('agregar/<str:producto_id>/', agregar_al_carrito, name='agregar_carrito'),
    path('carrito/', ver_carrito, name='carrito'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)