from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, MaintenanceViewSet, ReclamationViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'maintenance', MaintenanceViewSet)
router.register(r'reclamations', ReclamationViewSet)

urlpatterns = router.urls
