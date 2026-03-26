from django.db import models
from django.contrib.auth.models import AbstractUser

# --- USUARIOS (Integrado con el sistema de autenticación de Django) ---

class Usuario(AbstractUser):
    # AbstractUser ya incluye: password, is_active , email , first_name , last_name
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)
    creado_por = models.ForeignKey('cuentas.Cuenta', on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey('entidades.Departamento', on_delete=models.SET_NULL, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    foto_url = models.URLField(max_length=255, null=True, blank=True)
    plan = models.ForeignKey('entidades.Plan', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, null=True, blank=True)
    nacionalidad = models.CharField(max_length=50, null=True, blank=True)
    rol = models.CharField(max_length=50, default='GERENCIA')
