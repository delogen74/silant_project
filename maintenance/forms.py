from django import forms
from .models import TO

class TOForm(forms.ModelForm):
    """Форма для создания/редактирования записи ТО."""
    class Meta:
        model = TO
        fields = [
            'machine',
            'to_type',
            'date_performed',
            'operating_time',
            'order_number',
            'order_date',
            'organization',
            'service_company',
        ]