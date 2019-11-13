from django.db import models


class Local(models.Model):
    """
    Clase que representa un local comercial
    """
    nombre = models.CharField(max_length=250)
