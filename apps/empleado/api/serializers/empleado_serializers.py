
from rest_framework import serializers

from apps.empleado.models import Empleado
from apps.empleado.api.serializers.departamento_serializers import departamentoSerializer

class empleadoSerializer(serializers.ModelSerializer):
    codigo_departamento = departamentoSerializer

    class Meta:
        model=Empleado
        fields = '__all__'

    #def to_representation(self,instance):
    #        return {
    #            'codigo': instance.codigo,
    #            'nit':instance.nit,
    #            'nombre': instance.nombre,
    #            'apellido1': instance.apellido1,
    #            'apellido2': instance.apellido2,
    #            'codigo_departamento': instance.codigo_departamento.nombre if instance.codigo_departamento is not None else '',
    #            
    #        }