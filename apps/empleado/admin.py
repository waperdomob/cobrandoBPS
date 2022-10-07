from django.contrib import admin

from apps.empleado.models import Empleado, departamento

# Register your models here.
class departamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','presupuesto',)

admin.site.register(departamento,departamentoAdmin)
admin.site.register(Empleado)