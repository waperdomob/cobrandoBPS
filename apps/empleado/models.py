from django.db import models
from django.forms import model_to_dict

class departamento(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nit = models.CharField(max_length = 9, unique = True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido1 = models.CharField('Primer apellido',max_length = 100)
    apellido2 = models.CharField('Segundo apellido', max_length = 100, blank = True, null = True)
    codigo_departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return f'{self.nombre}'