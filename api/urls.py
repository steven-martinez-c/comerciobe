from django.conf.urls import url, include

urlpatterns = [
    url(r'^comercio/', include(('api.comercio.urls', 'api_comercio'), namespace='api_comercio')),
]
