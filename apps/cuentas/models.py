from django.db import models

class Cuenta(models.Model):
    # Definimos las constantes de los roles
    MASTER = 'MASTER'
    ADMIN = 'ADMIN'
    GERENCIA = 'GERENCIA'

    ROLES_CHOICES = [
        (MASTER, 'Master'),
        (ADMIN, 'Administrador'),
        (GERENCIA, 'Gerencia'),
    ]

    tipo_cuenta = models.CharField(
        max_length=15,
        choices=ROLES_CHOICES,
        default=GERENCIA, # Por seguridad, el rol más bajo por defecto
    )

    # Django crea el id (id_cuenta) automáticamente como AutoField
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # Nota: Para contraseñas de cuentas/empresas
    config_modulos = models.JSONField(null=True, blank=True)
    logo_url = models.URLField(max_length=255, null=True, blank=True)