from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.comercio import views

router = DefaultRouter()

router.register(r'local', views.LocalViewSet, base_name='Section')

urlpatterns = [
    url(r'^', include(router.urls)),
]
