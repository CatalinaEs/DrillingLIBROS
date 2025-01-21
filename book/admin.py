from django.contrib import admin
from .models import Libro, Libro1
# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valoracion', 'valor')  # Mostrar título, valoración y valor
    list_filter = ('valoracion', 'fecha_modificacion')  # Filtros por valoración y fecha de modificación
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')  # Campos de solo lectura

admin.site.register(Libro, LibroAdmin)


class LibroAdmin1(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'valoracion', 'obtener_valoracion')  # Mostrar el tipo de valoración

admin.site.register(Libro1, LibroAdmin1)