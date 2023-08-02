from rest_framework import generics, response, status, request, permissions
from .models import *
from .serializers import *

# clase para registrar un usuario


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

# esta clase devolvera el perfil del usuario ,al ingresar la token de acceso proporcionada por login


class PerfilUsuarioApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(sel, request: request.Request):
        print(request.user)
        print(request.auth)
        usuario_encontrado = MostrarUsuarioSerializer(instance=request.user)
        return response.Response(data={
            'message': f'Bienvenido, {request.user}',
            'content': usuario_encontrado.data
        })

# esta clase mostrara todas las categorias creadas


class MostrarCategoriasApiView(generics.ListAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer

# esta clase crea una categoria


class CrearCategoriaApiView(generics.CreateAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer

# esta clase se utiliza para mostrar una categoria al colocar el id correspondiente


class MostrarUnaCategoriaApiView(generics.RetrieveAPIView):
    def get(self, request, id):
        resultado = CategoriaModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'la categoria no existe'
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = CategoriaSerializer(instance=resultado)
        return response.Response(data={
            'message': serializador.data
        }, status=status.HTTP_200_OK)

# esta clase actualizara una categoria


class ActualizarCategoria(generics.RetrieveUpdateAPIView):
    def put(self, request: request.Request, id):
        resultado = CategoriaModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'La categoría no existe'
            }, status=status.HTTP_404_NOT_FOUND)

        data_serializada = CategoriaSerializer(data=request.data)

        if data_serializada.is_valid():
            resultado.nombre = (data_serializada.data.get('nombre'))
            resultado.save()
            return response.Response(data={
                'message': 'Categoria actualizada exitosamente'
            }, status=status.HTTP_200_OK)

        else:
            return response.Response(data={
                'message': 'Error al actualizar la categoria',
                'content': data_serializada.errors
            }, status=status.HTTP_400_BAD_REQUEST)

# esta clase elimina una categoria


class EliminarCategoria(generics.DestroyAPIView):
    def delete(self, request, id):
        resultado = CategoriaModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'La categoría no existe'
            }, status=status.HTTP_404_NOT_FOUND)

        resultado.delete()
        return response.Response(data={
            'message': 'Categoría eliminada exitosamente'
        }, status=status.HTTP_200_OK)
