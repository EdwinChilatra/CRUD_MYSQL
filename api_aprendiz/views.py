from django.http import JsonResponse
from django.views import View
from .models import Aprendiz
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class ApprenticeView(View):

    @method_decorator (csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self, request, id = 0):
        if(id > 0):
            Apprentices = list(Aprendiz.objects.filter(id=id).values())
            if len(Apprentices) > 0:
                apprentice = Apprentices[0]
                datos = {'message': 'Success', 'Apprentices': apprentice}
            else:
                datos = {'message': 'Aprendiz not found'}
        else:
            Apprentices = list(Aprendiz.objects.values())
            if len(Apprentices) > 0:
                datos = {'message': 'Success', 'Apprentices':Apprentices}
            else:
                datos = {'message': 'Apprentices not found...'}
        return JsonResponse(datos)
    
    def post (self, request) :
        js = json.loads(request.body)
        Aprendiz.objects.create(nombre =js['nombre'], 
                                apellido = js['apellido'], 
                                fecha_nacimiento = js['fecha_nacimiento'], 
                                numero_documento = js['numero_documento'], 
                                tipo_documento = js['tipo_documento'], 
                                numero_ficha = js['numero_ficha'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    
    def put (self,request, id):
        jd = json.loads(request.body)
        Apprentices = list(Aprendiz.objects.filter(id=id).values())
        if (len(Apprentices) > 0):
            aprendiz = Aprendiz.objects.get(id=id)
            aprendiz.nombre = jd['nombre']
            aprendiz.apellido = jd['apellido']
            aprendiz.fecha_nacimiento = jd['fecha_nacimiento']
            aprendiz.numero_documento = jd['numero_documento']
            aprendiz.tipo_documento = jd['tipo_documento']
            aprendiz.numero_ficha = jd['numero_ficha']
            aprendiz.save()

            datos = {'message': 'Success'}
        else:
            datos = {'message': 'apprentices not found...'}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        Apprentices = list(Aprendiz.objects.filter(id=id).values())
        if (len(Apprentices) > 0):
            Aprendiz.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'apprentices not found...'}
        
        return JsonResponse(datos)