from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=12)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return(f'{self.nombre}')
