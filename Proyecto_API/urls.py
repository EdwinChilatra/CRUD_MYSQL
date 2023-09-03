
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api_aprendiz/', include('api_aprendiz.urls')),
    path('api_pedidos/', include('api_pedidos.urls'))

    
]
