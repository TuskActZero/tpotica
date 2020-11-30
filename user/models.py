from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES =(
        (1, 'secretaria'),
        (2, 'gerencia'),
        (3, 'ventas'),
        (4, 'taller'),
        (5, 'profesionales'),
    )
    sector = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    asistencia = models.BooleanField(default=False)
    turno = models.OneToOneField('Turno', on_delete=models.CASCADE)
    historialMedico = models.OneToOneField('HistorialMedico', on_delete=models.CASCADE)

class Turno(models.Model):
    turno = models.DateTimeField()


class HistorialMedico(models.Model):
    historial_medico = models.TextField()


class Pedido(models.Model):
    nombre_producto = models.CharField(max_length=40)
    lejos = models.BooleanField(default=False)
    cerca = models.BooleanField(default=False)
    izquierda = models.BooleanField(default=False)
    derecha = models.BooleanField(default=False)
    armazon = models.BooleanField(default=False)
    id_lente = models.ForeignKey('Lente', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    pendiente = models.BooleanField(default=True)
    finalizado = models.BooleanField(default=False)

class Lente(models.Model):
    nombre_lente = models.CharField(max_length=30)
    precio = models.PositiveIntegerField()

# Usuarios

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    historialMedico = models.OneToOneField(HistorialMedico, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Secretaria(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Ventas(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Gerencia(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Taller(models.Model):
    nombre = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



