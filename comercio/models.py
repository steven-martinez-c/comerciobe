from django.db import models


class Local(models.Model):
    """
    Clase que representa un local comercial
    """
    nombre = models.CharField(max_length=250)


class Abuelo(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Padre(models.Model):
    nombre = models.CharField(max_length=250)
    abuelo = models.ForeignKey('Abuelo',
                               related_name='padres',
                               on_delete=models.CASCADE
                               )
    def __str__(self):
        return self.nombre


class Tio(models.Model):
    nombre = models.CharField(max_length=250)
    abuelo = models.ForeignKey('Abuelo',
                               related_name='tios',
                               on_delete=models.CASCADE
                               )
    def __str__(self):
        return self.nombre


class Primo(models.Model):
    nombre = models.CharField(max_length=250)
    tio = models.ForeignKey('Tio',
                            related_name='primos',
                            on_delete=models.CASCADE
                            )
    def __str__(self):
        return self.nombre


class Hijo(models.Model):
    nombre = models.CharField(max_length=250)
    padre = models.ForeignKey('Padre',
                              related_name='hijos',
                              on_delete=models.CASCADE
                              )
    def __str__(self):
        return self.nombre

    def abuelo(self):
        return self.padre.abuelo

    def tios(self):
        return self.abuelo().tios.all()

    def primos(self):
        # return Primo.objects.filter(tio__in=self.tios())
        return Primo.objects.filter(tio__in=self.padre.abuelo.tios.all())