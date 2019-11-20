from django.contrib import admin

from comercio.models import Local, Seccion, Producto, OfertaProducto, Valoracion

admin.site.register(Local)
admin.site.register(Seccion)
admin.site.register(Producto)
admin.site.register(OfertaProducto)
admin.site.register(Valoracion)