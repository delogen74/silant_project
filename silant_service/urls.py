from django.contrib import admin
from django.urls import path, include
from machines.views import guest_search, main_dashboard, machines_list, machine_create, machine_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guest_search, name='guest-search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', main_dashboard, name='main-dashboard'),
    path('machines/', machines_list, name='machines-list'),
    path('machines/create/', machine_create, name='machine-create'),
    path('machines/edit/<int:pk>/', machine_edit, name='machine-edit'),
    path('claims/', include('claims.urls')),
    path('to/', include('maintenance.urls')),
    path('api/', include('api.urls')),
]
