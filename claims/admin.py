from django.contrib import admin
from .models import Reclamation

@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('failure_date', 'failure_node', 'machine', 'service_company', 'downtime')
    search_fields = ('failure_node', 'machine__factory_number', 'service_company')

