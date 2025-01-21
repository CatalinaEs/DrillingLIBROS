from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valoracion = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
    
class Libro1(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    valoracion = models.DecimalField(max_digits=5, decimal_places=2)  # Este es el campo de valoración

    def __str__(self):
        return self.titulo

    # Campo dinámico para mostrar la valoración
    def obtener_valoracion(self):
        if self.valoracion < 1000:
            return 'Baja'
        elif 1000 <= self.valoracion <= 2500:
            return 'Media'
        else:
            return 'Alta'