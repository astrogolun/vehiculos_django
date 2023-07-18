from django.contrib import admin

# Register your models here.

from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    pass


