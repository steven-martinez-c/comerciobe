from rest_framework import serializers

from comercio.models import Local, Seccion, Producto, OfertaProducto, Valoracion


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class OfertaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaProducto
        fields = '__all__'


class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'
