from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/productos/')),  # Redirige la raíz a /productos/
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
]