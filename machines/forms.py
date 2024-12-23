# machines/forms.py
from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):
    """
    Форма для создания/редактирования объекта Machine.
    Поля: заводской номер, модель, клиент, сервисная компания и т.д.
    """
    class Meta:
        model = Machine
        fields = [
            'factory_number',
            'machine_model',
            'engine_model',
            'engine_number',
            'transmission_model',
            'transmission_number',
            'drive_axle_model',
            'drive_axle_number',
            'steerable_axle_model',
            'steerable_axle_number',
            'shipment_date',
            'consignee',
            'delivery_address',
            'equipment',
            'client',
            'service_company',
        ]
