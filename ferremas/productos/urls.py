from django.urls import path
from . import views # Importamos las vistas de la aplicación productos

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/crear/', views.crear, name='crear'),
    path('productos/editar/', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)