from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not None is False:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not None is False:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    username = None # Eliminamos username definitivamente
    email = models.EmailField('email address', unique=True)
    
    # RELACIÓN: Cada usuario pertenece a una Cuenta
    cuenta = models.ForeignKey(
        'cuentas.Cuenta', 
        on_delete=models.CASCADE, 
        related_name='usuarios',
        null=True, 
        blank=True
    )
    
    rol_interno = models.CharField(max_length=50, blank=True) 
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True)

    # AQUÍ ESTÁ EL TRUCO:
    objects = UsuarioManager() # Le decimos a Django que use nuestro nuevo Manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Ya no pedirá username nunca más

    def __str__(self):
        return self.email