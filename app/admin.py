from django.contrib import admin
from .models import Usuario,Producto,Sede,Almacen,Depart,Cargo,Operador,equipo_asignado,almacenamiento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Sede)
admin.site.register(Almacen)
admin.site.register(Depart)
admin.site.register(Cargo)
admin.site.register(Operador)
admin.site.register(equipo_asignado)
admin.site.register(almacenamiento)