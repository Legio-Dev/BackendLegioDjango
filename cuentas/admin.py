from django.contrib import admin
from .models import Cuenta

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_cuenta', 'email', 'activo')
    list_filter = ('tipo_cuenta', 'activo')
    search_fields = ('nombre', 'email')