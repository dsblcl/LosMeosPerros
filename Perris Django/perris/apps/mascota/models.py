from django.db import models

from apps.adopcion.models import Persona
# Create your models here.
ESTADOS= (
    ('Rescatado', 'Rescatado'),
    ('Disponible', 'Disponible'),
    ('Adoptado', 'Adoptado'),)

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def str(self):
        return '{}'.format(self.nombre)



class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    foto= models.ImageField(upload_to = 'photos/',null=True)
    Descripcion = models.TextField( null=True)
    fecha_rescate = models.DateField()
    estado= models.CharField(max_length=30, choices=ESTADOS, default='')
