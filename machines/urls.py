from django.urls import path
from .views import machine_list, machine_create, machine_edit

urlpatterns = [
    path('', machine_list, name='machine-list'),
    path('create/', machine_create, name='machine-create'),
    path('edit/<int:pk>/', machine_edit, name='machine-edit'),
]
