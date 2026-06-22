from django.contrib import admin
from .models import UsuarioPerfil, Materia, Curso, HorarioClase

@admin.register(UsuarioPerfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'email', 'rol')
    list_filter = ('rol',)
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('anio', 'division', 'turno')
    list_filter = ('turno', 'anio')

@admin.register(HorarioClase)
class HorarioClaseAdmin(admin.ModelAdmin):
    list_display = ('curso', 'materia', 'docente', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'curso')