from rest_framework.routers import SimpleRouter

from inventory.views import BranchViewSet, VehiclePricingViewSet

app_name = 'inventory'

router = SimpleRouter()
router.register('branch', BranchViewSet, basename='branch')
router.register('pricing', VehiclePricingViewSet, basename='pricing')
