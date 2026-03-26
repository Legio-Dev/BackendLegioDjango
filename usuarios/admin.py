from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Esta configuración hace que Django use sus formularios de seguridad automáticos
class CustomUserAdmin(UserAdmin):
    model = Usuario
    # Aquí defines qué columnas ver en la tabla principal
    list_display = ['username', 'email', 'rol', 'is_staff']
    
    # Esto organiza tus campos personalizados (rol, codigo, etc) en secciones
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('rol', 'codigo', 'creado_por', 'departamento')}),
    )

admin.site.register(Usuario, CustomUserAdmin)