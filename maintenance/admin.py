from django.contrib import admin
from .models import TO

@admin.register(TO)
class TOAdmin(admin.ModelAdmin):
    list_display = ('to_type', 'date_performed', 'machine', 'service_company')
    search_fields = ('to_type', 'machine__factory_number', 'service_company')

