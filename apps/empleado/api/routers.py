from rest_framework.routers import DefaultRouter

from apps.empleado.api.viewsets.empleado_viewset import EmpleadoViewSet
from apps.empleado.api.viewsets.departamento_viewset import departamentoViewset

router = DefaultRouter()

router.register(r'empleados',EmpleadoViewSet, basename = 'empleados')
router.register(r'departamentos',departamentoViewset, basename = 'departamentos')


urlpatterns = router.urls

