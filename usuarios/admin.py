from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    
    # Eliminamos 'username' y 'rol' temporalmente de aquí si da error
    # Una vez que la migración funcione, puedes volver a agregar 'rol'
    list_display = ['email', 'is_staff', 'is_active'] 
    
    # Forzamos el orden por email, ya que username no existe
    ordering = ('email',)

    # Organizamos los campos para el formulario de edición
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # Comenta esta sección si 'rol' o 'codigo' te siguen dando error E108
        # ('Extra', {'fields': ('rol', 'codigo', 'cuenta')}), 
    )

    # Esto es para el formulario de CREAR usuario nuevo
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )

admin.site.register(Usuario, CustomUserAdmin)