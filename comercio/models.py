from django.contrib.auth.models import User
from django.db import models


class Local(models.Model):
    """
    Clase que representa un local comercial
    """
    nombre = models.CharField(max_length=250)

    class Meta:
        ordering = ['nombre']


class Seccion(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=400, null=True, blank=True)
    local = models.ForeignKey('comercio.Local', related_name='secciones', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.nombre


class OfertaProducto(models.Model):
    activo = models.BooleanField(default=True)
    desde = models.DateField()
    hasta = models.DateField(null=True, blank=True)
    producto = models.ForeignKey('comercio.Producto', related_name="ofertas_producto", on_delete=models.CASCADE)
    seccion = models.ForeignKey('comercio.Seccion', related_name="ofertas_producto", on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % {self.producto}


class Valoracion(models.Model):
    detalle = models.TextField(max_length=400, null=True, blank=True)
    valor = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    oferta_producto = models.ForeignKey('OfertaProducto', related_name='valoraciones', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="valoraciones", on_delete=models.CASCADE)

    def __str__(self):
        return self.detalle
