from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import LoginFormulario
from .models import Usuario
from .models import Producto
from .models import Opciones
from .models import Cliente
from .models import Factura
from .models import DetalleFactura
from .models import Proveedor
from .models import Pedido
from .models import DetallePedido
from .models import Notificaciones

class UsuarioAdmin(UserAdmin):
    add_form = LoginFormulario
    #form = CustomUserChangeForm
    model = Usuario
    list_display = ['email', 'username',]

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto)
admin.site.register(Opciones)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Notificaciones)