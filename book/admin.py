from django.contrib import admin
from .models import Libro
# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'valoracion')  # Mostrar título, valor y valoración
    list_filter = ('valoracion', 'fecha_modificacion')  # Filtros por valoración y fecha de modificación
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')  # Campos de solo lectura

admin.site.register(Libro, LibroAdmin)