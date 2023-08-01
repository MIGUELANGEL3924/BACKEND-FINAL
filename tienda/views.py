from rest_framework import generics, response, status, request
from .models import *
from .serializers import *


class RegistroUsuarioApiView(generics.CreateAPIView):
    def post(self, request: request.Request):
        serializador = RegistroUsuarioSerializer(data=request.data)

        if serializador.is_valid():
            nuevo_usuario = UsuarioModel(**serializador.validated_data)
            nuevo_usuario.set_password(
                serializador.validated_data.get('password'))

            nuevo_usuario.save()
            return response.Response(data={
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message': 'Error al registrar al usuario',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
