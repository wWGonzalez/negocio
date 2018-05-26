from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 75)
    address = models.CharField(max_length = 150)
    telephone = models.CharField(max_length = 12)
    picture = models.ImageField(upload_to = 'pictures')
    registered_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.name, self.telephone)

class Persona(models.Model):
    # person data
    # dpi = models.CharField(max_length = 20, blank = True)
    nombre = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 15)
    # alert data
    coordenadas = models.CharField(max_length = 200)
    direccion = models.CharField(max_length = 250)
    tipo_negocio = models.CharField(max_length = 50)

    def __str__(self):
        return '%s %s %s' % (self.dpi, self.nombre, self.telefono)
