from django.contrib import admin

# Register your models here.
from inmueble.models import Servicio, Casa

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ['nombre']

class CasaAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['en_venta', 'en_alquiler', 'moneda']
    autocomplete_fields = ['servicios', 'inmobiliaria']

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Casa, CasaAdmin)

