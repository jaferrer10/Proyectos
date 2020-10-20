from django.db import models

# Create your models here.

class Inmobiliaria(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


