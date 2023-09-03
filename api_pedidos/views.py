from django.http import JsonResponse
from django.views import View
from .models import Pedidos
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class PedidosView(View):
    
    @method_decorator (csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self, request, id = 0):
        if(id > 0):
            pedidos = list(Pedidos.objects.filter(id=id).values())
            if len(pedidos) > 0:
                pedido = pedidos[0]
                datos = {'Mensaje': 'Exito', 'Pedidos': pedido}
            else:
                datos = {'Mensaje': 'Pedido no encontrado'}
        else:
            pedidos = list(Pedidos.objects.values())
            if len(pedidos) > 0:
                datos = {'Mensaje': 'Exito', 'Pedidos':pedidos}
            else:
                datos = {'Mensaje': 'Pedidos no encontrados...'}
        return JsonResponse(datos)
    
    def post (self, request) :
        js = json.loads(request.body)
        Pedidos.objects.create(nombre_producto =js['nombre_producto'], 
                                cantidad = js['cantidad'], 
                                precio_unitario = js['precio_unitario'], 
                                numero_pedido = js['numero_pedido'], 
                                fecha_hora = js['fecha_hora'], 
                                estado_pedido = js['estado_pedido'],
                                total_pagar_pedido = js['total_pagar_pedido'])
        datos = {'Mensaje': 'Exito'}
        return JsonResponse(datos)
    
    def put (self,request, id):
        jd = json.loads(request.body)
        pedidos = list(Pedidos.objects.filter(id=id).values())
        if (len(pedidos) > 0):
            pedido = Pedidos.objects.get(id=id)
            pedido.nombre_producto = jd['nombre_producto']
            pedido.cantidad = jd['cantidad']
            pedido.precio_unitario = jd['precio_unitario']
            pedido.numero_pedido = jd['numero_pedido']
            pedido.fecha_hora = jd['fecha_hora']
            pedido.estado_pedido = jd['estado_pedido']
            pedido.total_pagar_pedido = jd['total_pagar_pedido']
            pedido.save()

            datos = {'Mensaje': 'Exito'}
        else:
            datos = {'Mensaje': 'Pedidos no encontrados...'}
        
        return JsonResponse(datos)
    
    def delete(self, request, id):
        pedidos = list(Pedidos.objects.filter(id=id).values())
        if (len(pedidos) > 0):
            Pedidos.objects.filter(id=id).delete()
            datos = {'Mensaje': 'Exito'}
        else:
            datos = {'Mensaje': 'Pedido no encontrado'}
        
        return JsonResponse(datos)
    
