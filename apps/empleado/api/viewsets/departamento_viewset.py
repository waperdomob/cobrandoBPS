from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.empleado.api.serializers.departamento_serializers import departamentoSerializer
from apps.empleado.models import departamento


class departamentoViewset(viewsets.ModelViewSet):
    serializer_class = departamentoSerializer
    
    def get_queryset(self, pk=None):
        if pk ==None:
            return departamento.objects.all()
        else:
            return departamento.objects.filter(codigo=pk).first()

    def list(self, request):
        departamento_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "departamentos": departamento_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer =  self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'departamento agregado con exito!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        departamento = self.get_queryset(pk)
        if departamento:
            departamento_serializer = self.serializer_class(departamento)
            return Response(departamento_serializer.data, status= status.HTTP_200_OK)
        return Response({'error':'No existe un departamento con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            departamento_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if departamento_serializer.is_valid():                
                departamento_serializer.save()
                return Response(departamento_serializer.data, status= status.HTTP_200_OK)
            return Response(departamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        departamento = self.get_queryset().filter(codigo=pk).first()
        if departamento:
            departamento.delete()
            return Response({'message':'departamento eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un departamento con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
