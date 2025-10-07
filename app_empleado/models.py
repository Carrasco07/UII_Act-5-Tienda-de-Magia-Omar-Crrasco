from django.db import models

# Create your models here.
# Clase Empleado con campo nombre, edad y email
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField(unique=True)

    


