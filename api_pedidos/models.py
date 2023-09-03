from django.db import models

class Pedidos(models.Model):
    nombre_producto = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits= 10, decimal_places=5) 
    numero_pedido = models.IntegerField()
    fecha_hora = models.DateTimeField()
    estado_pedido = models.CharField(max_length=10)
    total_pagar_pedido = models.DecimalField(max_digits= 10, decimal_places=5)