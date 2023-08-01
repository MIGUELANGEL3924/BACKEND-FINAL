from rest_framework import serializers
from .models import *


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'
