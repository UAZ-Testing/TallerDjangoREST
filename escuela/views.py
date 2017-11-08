from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from escuela.models import Escuela
from escuela.serializers import EscuelaSerializer
from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class ApiEscuela():
    @api_view(['GET'])
    def get_all(request):
        queryset = Escuela.objects.all()
        serializer = EscuelaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET', 'PUT', 'DELETE'])
    def manage_by_id(request, id_escuela):
        if request.method == 'GET':
            return ApiEscuela.get_by_id(request, id_escuela)
        elif request.method == 'PUT':
            return ApiEscuela.update(request, id_escuela)
        elif request.method == 'DELETE':
            return ApiEscuela.delete(request, id_escuela)

    def get_by_id(request, id_escuela):
        queryset = Escuela.objects.get(id_escuela=id_escuela)
        serializer = EscuelaSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(request, id_escuela):
        escuela = Escuela.objects.get(id_escuela=id_escuela)
        serializer = EscuelaSerializer(escuela)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(request, id_escuela):
        escuela = Escuela.objects.get(id_escuela=id_escuela)
        escuela.delete()
        return Response('Escuela eliminada', status=status.HTTP_200_OK)


'''
class ApiEscuela(APIView):
    def get(self, request):
        queryset = Escuela.objects.all()
        serializer = EscuelaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EscuelaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Escuela guardada', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiEscuelaMixins(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApiEscuela2(APIView):
    def get_object(self, id_escuela):
        try:
            return Escuela.objects.get(id_escuela=id_escuela)
        except Escuela.DoesNotExist:
            raise Http404

    def delete(self, request, id_escuela):
        escuela = self.get_object(id_escuela)
        escuela.delete()
        return Response('Escuela eliminada', status=status.HTTP_200_OK)

    def put(self, request, id_escuela):
        escuela = self.get_object(id_escuela)
        serializers = EscuelaSerializer(escuela, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response('Escuela guardada', status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
'''
