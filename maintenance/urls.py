from django.urls import path
from .views import to_list, to_create, to_edit

urlpatterns = [
    path('', to_list, name='to-list'),
    path('create/', to_create, name='to-create'),
    path('create/<int:machine_id>/', to_create, name='to-create-for-machine'),
    path('edit/<int:pk>/', to_edit, name='to-edit'),
]
