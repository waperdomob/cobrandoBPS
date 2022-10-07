from rest_framework import serializers

from apps.empleado.models import departamento

class departamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = departamento
        fields = '__all__'
