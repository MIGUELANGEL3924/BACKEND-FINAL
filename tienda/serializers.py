from rest_framework import serializers
from .models import *


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'


class MostrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        exclude = ['password', 'is_staff', 'user_permissions',
                   'groups', 'last_login', 'is_superuser']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField()

    class Meta:
        model = ProductoModel
        fields = '__all__'
