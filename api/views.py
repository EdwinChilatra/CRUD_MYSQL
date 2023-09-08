from django.http import JsonResponse
from django.views import View
from .models import Company, Developers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': 'Success', 'companies': company}
            else:
                datos = {'message': 'Company not found'}
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': 'Success', 'companies':companies}
            else:
                datos = {'message': 'companies not found...'}
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if (len(companies) >0 ):
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()

            datos = {'message': 'Success'}
        else:
            datos = {'message': 'companies not found...'}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list (Company.objects.filter(id=id).values())
        if (len(companies) > 0):
            Company.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'company not found...'}
        
        return JsonResponse(datos)
            
class DeveloperView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self, request, id = 0):
        if(id > 0):
            developer = Developers.objects.get(id = id)
            if developer:
                datos = {'message': 'Success', 'companies': developer}
            else:
                datos = {'message': 'Company not found...'}
        else:
            developers = list(Developers.objects.values())
            if (len(developers) > 0):
                datos = {'message': 'Success', 'developers': developers}
            else:
                datos = {'message': 'Developers not found...'}

        return JsonResponse (datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        company = Company.objects.get(id = jd['company'])
        Developers.objects.create(name=jd['name'], company=company)
        datos = {'message': 'Success'}
        return JsonResponse(datos)
     
    def put(self, request, id):
        jd = json.loads(request.body)
        developers = list(Developers.objects.filter(id=id).values())
        if (len(developers) >0 ):
            developer = Developers.objects.get(id=id)
            company = Company.objects.get(id =jd ['company'])
            developer.name = jd['name']
            developer.company = company
            developer.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Developers not found...'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        developers = list(Developers.objects.filter(id=id).values())
        if len(developers) > 0:
            Developers.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Developer not found...'}
        return JsonResponse(datos)