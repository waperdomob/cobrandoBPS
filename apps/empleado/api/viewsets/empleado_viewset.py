from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.empleado.models import Empleado
from apps.empleado.api.serializers.empleado_serializers import empleadoSerializer



class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = empleadoSerializer

    def get_queryset(self, pk=None):
        if pk ==None:
            return Empleado.objects.all()
        else:
            return Empleado.objects.filter(codigo=pk).first()

    def list(self, request):
        empleado_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "empleados": empleado_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer =  self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empleado agregado con exito!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        empleado = self.get_queryset(pk)
        if empleado:
            empleado_serializer = self.serializer_class(empleado)
            return Response(empleado_serializer.data, status= status.HTTP_200_OK)
        return Response({'error':'No existe un empleado con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            empleado_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if empleado_serializer.is_valid():                
                empleado_serializer.save()
                return Response(empleado_serializer.data, status= status.HTTP_200_OK)
            return Response(empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        empleado = self.get_queryset().filter(codigo=pk).first()
        if empleado:
            empleado.delete()
            return Response({'message':'empleado eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un empleado con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
