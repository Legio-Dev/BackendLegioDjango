from django.db import models
from django.contrib.auth.models import AbstractUser

# --- TABLAS DE ENTIDAD BASE ---

class Cuenta(models.Model):
    # Django crea el id (id_cuenta) automáticamente como AutoField
    tipo_cuenta = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # Nota: Para contraseñas de cuentas/empresas
    config_modulos = models.JSONField(null=True, blank=True)
    logo_url = models.URLField(max_length=255, null=True, blank=True)

class Locacion(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='locaciones')
    activo = models.BooleanField(default=True)
    direccion = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=100)
    mail_notificacion = models.JSONField(null=True, blank=True)

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField()
    locaciones_ids = models.JSONField()

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

class MotivoVisita(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

class RazonVisita(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

class TipoInvitacion(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    tipo = models.CharField(max_length=30, null=True, blank=True)

# --- USUARIOS (Integrado con el sistema de autenticación de Django) ---

class Usuario(AbstractUser):
    # AbstractUser ya incluye: password, is_active , email , first_name , last_name
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)
    creado_por = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    foto_url = models.URLField(max_length=255, null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, null=True, blank=True)
    nacionalidad = models.CharField(max_length=50, null=True, blank=True)
    rol = models.CharField(max_length=50, default='GERENCIA')

# --- TABLA OPERACIONAL ---

class Invitacion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=255)
    celular_contacto = models.CharField(max_length=20)
    correo_contacto = models.EmailField(max_length=255)
    locacion = models.ForeignKey(Locacion, on_delete=models.SET_NULL, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    tipo_invitacion = models.ForeignKey(TipoInvitacion, on_delete=models.SET_NULL, null=True)
    motivo = models.ForeignKey(MotivoVisita, on_delete=models.SET_NULL, null=True)
    detalles = models.TextField(null=True, blank=True)
    estado_invitacion = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10, null=True, blank=True)
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    foto_rostro_url = models.URLField(max_length=255, null=True, blank=True)
    tipo_ingreso = models.CharField(max_length=50, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    foto_vehiculo_url = models.URLField(max_length=255, null=True, blank=True)
    equipo = models.BooleanField(default=False)
    foto_equipo_url = models.URLField(max_length=255, null=True, blank=True)
    documentos = models.BooleanField(default=False)
    documentos_zip = models.URLField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ingreso = models.DateTimeField(null=True, blank=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)