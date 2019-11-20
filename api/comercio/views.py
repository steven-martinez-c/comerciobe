# GET (Obtener 1 o muchos objetos)
# --> list (lista los objetosobjetos)
# --> retrieve (lista un objetos)
# POST (Crear 1 o muchos objetos)
# --> create (crea un objeto)
# PUT, PATCH (Modificar Objetos
# --> update (put: actualiza un objeto)
# --> partial_update (path: actualiza un objeto para solo los campos que enviamos)
# DELETE (Eliminar 1 o mas objetos)
# --> destroy (borra un objeto)
from rest_framework import viewsets

from api.comercio.serializers import LocalSerializer, SeccionSerializer, ProductoSerializer, OfertaProductoSerializer, \
    ValoracionSerializer
from comercio.models import Local, Valoracion, OfertaProducto, Producto, Seccion


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class OfertaProductoViewSet(viewsets.ModelViewSet):
    queryset = OfertaProducto.objects.all()
    serializer_class = OfertaProductoSerializer


class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
