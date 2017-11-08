from escuela.models import Escuela
from rest_framework import serializers


class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ('id_escuela', 'nombre', 'direccion')
