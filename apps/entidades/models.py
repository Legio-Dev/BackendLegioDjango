from django.db import models

class Locacion(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey('cuentas.Cuenta', on_delete=models.CASCADE, related_name='locaciones')
    activo = models.BooleanField(default=True)
    direccion = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=100)
    mail_notificacion = models.JSONField(null=True, blank=True)

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey('cuentas.Cuenta', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField()
    locaciones_ids = models.JSONField()

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    creado_por = models.ForeignKey('cuentas.Cuenta', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

class MotivoVisita(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

class RazonVisita(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)