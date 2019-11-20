from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.comercio import views

router = DefaultRouter()

router.register(r'local', views.LocalViewSet, base_name='local')
router.register(r'seccion', views.SeccionViewSet, base_name='seccion')
router.register(r'producto', views.ProductoViewSet, base_name='producto')
router.register(r'oferta_producto', views.OfertaProductoViewSet, base_name='oferta_producto')
router.register(r'valoracion', views.ValoracionViewSet, base_name='valoracion')

urlpatterns = [
    url(r'^', include(router.urls)),
]
