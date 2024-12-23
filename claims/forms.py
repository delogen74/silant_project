from django import forms
from .models import Reclamation

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = [
            'machine',
            'failure_date',
            'operating_time',
            'failure_node',
            'failure_description',
            'recovery_method',
            'used_parts',
            'recovery_date',
            'downtime',
            'service_company',
        ]
