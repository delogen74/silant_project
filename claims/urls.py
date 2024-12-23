from django.urls import path
from .views import reclamation_list, reclamation_create, reclamation_edit

urlpatterns = [
    path('', reclamation_list, name='reclamation-list'),
    path('create/', reclamation_create, name='reclamation-create'),
    path('edit/<int:pk>/', reclamation_edit, name='reclamation-edit'),
]
