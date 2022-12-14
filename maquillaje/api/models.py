from django.db import models

from django.contrib.auth.models import User # importamos la clase user que es la clase donde se vban a logear los users por default

class Productos(models.Model):
    nombre = models.CharField(max_length=15,null=True)
    marca = models.CharField(max_length=15,null=True)
    cantidad = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "productos"
    
    