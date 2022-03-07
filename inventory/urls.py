from rest_framework.routers import SimpleRouter

from inventory.views import BranchViewSet, VehiclePricingViewSet, InventoryViewSet

app_name = 'inventory'

router = SimpleRouter()
router.register('branch', BranchViewSet, basename='branch')
router.register('pricing', VehiclePricingViewSet, basename='pricing')
router.register('inventory', InventoryViewSet, basename='inventory')

urlpatterns = [] + router.urls
