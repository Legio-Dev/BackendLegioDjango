from django.db import models

class Cuenta(models.Model):
    # Usamos constantes para evitar errores de dedo ("Gerente" vs "GERENCIA")
    MASTER = 'MASTER'
    ADMIN = 'ADMIN'
    GERENCIA = 'GERENCIA'

    TIPO_CHOICES = [
        (MASTER, 'Master (Legio Access)'),
        (ADMIN, 'Administrador (Cliente)'),
        (GERENCIA, 'Gerencia (Solo Lectura)'),
    ]

    nombre = models.CharField(max_length=100)
    tipo_cuenta = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES, 
        default=GERENCIA
    )
    email = models.EmailField(unique=True)
    # Si esta password es para un login de la "Empresa", guárdala, 
    # pero recuerda que los empleados usarán su propio usuario.
    password = models.CharField(max_length=255) 
    activo = models.BooleanField(default=True)
    config_modulos = models.JSONField(null=True, blank=True, default=dict)
    logo_url = models.URLField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_cuenta}"