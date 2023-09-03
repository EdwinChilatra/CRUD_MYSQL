from django.urls import path
from .views import PedidosView

urlpatterns = [
    path('pedidos/', PedidosView.as_view(), name='pedidos_list'),
    path('pedidos/<int:id>', PedidosView.as_view()),
    path('pedidos/put/', PedidosView.as_view()),
    path('pedidos/delete/', PedidosView.as_view()),


]