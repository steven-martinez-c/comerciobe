from django.db import models


class Local(models.Model):
    """
    Clase que representa un local comercial
    """
    nombre = models.CharField(max_length=250)


class Abuelo(models.Model):
    nombre = models.CharField(max_length=250)


class Padre(models.Model):
    nombre = models.CharField(max_length=250)
    abuelo = models.ForeignKey('Abuelo',
                               related_name='padres',
                               on_delete=models.CASCADE
                               )


class Tio(models.Model):
    nombre = models.CharField(max_length=250)
    abuelo = models.ForeignKey('Abuelo',
                               related_name='tios',
                               on_delete=models.CASCADE
                               )


class Primo(models.Model):
    nombre = models.CharField(max_length=250)
    tio = models.ForeignKey('Tio',
                            related_name='primos',
                            on_delete=models.CASCADE
                            )


class Hijo(models.Model):
    nombre = models.CharField(max_length=250)
    padre = models.ForeignKey('Padre',
                              related_name='hijos',
                              on_delete=models.CASCADE
                              )
    def abuelo(self):
        return self.padre.abuelo

    def tios(self):
        return self.abuelo().tios.all()
