from .models import Gato
from rest_framework import serializers


class GatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gato
        fields = ('nombre', 'raza', 'nacimiento', 'sexo')
