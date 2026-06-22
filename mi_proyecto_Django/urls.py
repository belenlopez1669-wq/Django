from django.contrib import admin
from django.urls import path
from mi_pagina_codee import views  # Importamos tus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),                                 # Página principal
    path('docentes/', views.ver_docentes, name='ver_docentes'),           # URL para docentes
    path('materias/', views.ver_materias, name='ver_materias'),           # URL para materias
    path('administrador/', views.ver_administrador, name='ver_configuracion'), # URL para configuración
]