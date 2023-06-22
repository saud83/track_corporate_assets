from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, LogViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'logs', LogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]