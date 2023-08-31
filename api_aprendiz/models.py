from django.db import models

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=4)
    numero_ficha =models.PositiveIntegerField()
