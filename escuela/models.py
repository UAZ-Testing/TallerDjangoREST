from django.db import models


# Create your models here.

class Escuela(models.Model):
    id_escuela = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela)
