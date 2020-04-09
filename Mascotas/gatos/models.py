from django.db import models

# Create your models here.

class Gato(models.Model):

    RAZAS = (
        ('C', 'Callejero'),
        ('A', 'Angora'),
        ('S', 'Siames'),
    )

    SEXO = (
        ('F', 'Femenino'),
        ('M','Masculino'),
        
    )

    nombre = models.CharField(max_length=100,blank=True, null=True)
    raza = models.CharField(max_length=50,blank=True, null=True, choices=RAZAS)
    nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=100, blank=True, null=True, choices=SEXO)

    def __str__(self):
        return self.nombre