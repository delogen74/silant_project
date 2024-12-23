from rest_framework.viewsets import ModelViewSet
from machines.models import Machine
from maintenance.models import Maintenance
from claims.models import Reclamation
from .serializers import MachineSerializer, MaintenanceSerializer, ReclamationSerializer

class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MaintenanceViewSet(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class ReclamationViewSet(ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
