from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class InmuebleBase(models.Model):
    class Meta:
        verbose_name = 'Inmueble Base'
        abstract = True

    PESO = 'peso'
    DOLAR = 'dolar'
    EURO = 'euro'
    REAL = 'real'

    MONEDAS = [
        (PESO, 'Peso'),
        (DOLAR, 'Dólar'),
        (EURO, 'Euro'),
        (REAL, 'Real')
    ]

    nombre = models.CharField(max_length=80)
    medidas = models.CharField(max_length=30, blank=True)
    moneda = models.CharField(max_length=5, choices=MONEDAS, default=PESO)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    descripcion = models.TextField(blank=True)
    en_venta = models.BooleanField(default=False)
    en_alquiler = models.BooleanField(default=False)

    # Relaciones
    servicios = models.ManyToManyField(Servicio, blank=True)
    inmobiliaria = models.ForeignKey(
        'inmobiliaria.Inmobiliaria',
        on_delete=models.CASCADE, blank=True, null=True,
        related_name='casas'
    )

    def __str__(self):
        return self.nombre


class Casa(InmuebleBase):
    class Meta:
        verbose_name = 'Lista de casa'
        verbose_name_plural = 'Listado de casas'

    cantidad_habitaciones = models.PositiveSmallIntegerField(default=0)
    cantidad_banios = models.PositiveSmallIntegerField(default=0)
    cantidad_suite = models.PositiveSmallIntegerField(default=0)