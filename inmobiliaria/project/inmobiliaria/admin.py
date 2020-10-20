from django.contrib import admin

# Register your models here.
from inmobiliaria.models import Inmobiliaria


class InmobiliariaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo_electronico']
    search_fields = ['nombre']


admin.site.register(Inmobiliaria, InmobiliariaAdmin)

