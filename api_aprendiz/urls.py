from django.urls import path
from .views import ApprenticeView

urlpatterns = [
    path('apprentices/', ApprenticeView.as_view(), name='apprentice_list'),
    path('apprentices/<int:id>', ApprenticeView.as_view()),
    path('apprentices/put/', ApprenticeView.as_view()),
    path('apprentices/delete/', ApprenticeView.as_view()),


]