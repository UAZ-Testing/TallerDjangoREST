from escuela.models import Escuela, Estudiante
from rest_framework import serializers


class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ('id_escuela', 'nombre', 'direccion')


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id_estudiante', 'nombre', 'escuela')
