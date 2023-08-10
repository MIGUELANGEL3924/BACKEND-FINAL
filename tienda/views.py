from django.shortcuts import render, HttpResponse
from rest_framework import generics, response, status, request, permissions
from .models import *
from .serializers import *
from .permissions import SoloAdministrador


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
    permission_classes = [permissions.IsAuthenticated]
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer
# esta clase crea una categoria


class CrearCategoriaApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer
# esta clase se utiliza para mostrar una categoria al colocar el id correspondiente


class MostrarUnaCategoriaApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]

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
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]

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

# esta clase mostrara una lista de todos los productos creados


class ListaProductosApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer
# esta clase creara un producto:


class CrearProductoApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]

    def post(self, request: request.Request):
        form_data = request.data
        dic_data = {
            'nombre': form_data.get('nombre'),
            'precio': form_data.get('precio'),
            'cantidad': form_data.get('cantidad'),
            'imagen': request.FILES.get('imagen'),
            'categoria': form_data.get('categoria')
        }
        serializador = ProductoSerializer(data=dic_data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return response.Response(data={
                'message': 'Producto creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        except Exception as err:
            return response.Response(data={
                'message': 'Error al crear el producto',
                'content': err.args
            }, status=status.HTTP_400_BAD_REQUEST)
# esta clase mostrara un producto


class MostrarUnProductoApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        resultado = ProductoModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'el producto no existe'
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(instance=resultado)
        return response.Response(data={
            'message': serializador.data
        }, status=status.HTTP_200_OK)
# esta clase actualizara un producto


class ActualizarProductoApiView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer

    def put(self, request, *args, **kwargs):
        # Obtener el ID del producto desde los parámetros de la URL
        id = kwargs.get('id')
        try:
            # Obtener el objeto del producto por su ID
            instance = self.get_queryset().get(id=id)
        except ProductoModel.DoesNotExist:
            return response.Response(data={
                'message': 'Producto no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        form_data = request.data
        dic_data = {
            'nombre': form_data.get('nombre'),
            'precio': form_data.get('precio'),
            'cantidad': form_data.get('cantidad'),
            'imagen': request.FILES.get('imagen'),
            'categoria': form_data.get('categoria')
        }
        serializador = self.get_serializer(
            instance, data=dic_data, partial=True)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return response.Response(data={
                'message': 'Producto actualizado exitosamente'
            }, status=status.HTTP_200_OK)
        except Exception as err:
            return response.Response(data={
                'message': 'Error al actualizar el producto',
                'content': err.args
            }, status=status.HTTP_400_BAD_REQUEST)
# esta clase eliminara un producto


class EliminarProductoApiView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer

    def delete(self, request, *args, **kwargs):
        # Obtener el ID del producto desde los parámetros de la URL
        id = kwargs.get('id')
        try:
            # Obtener el objeto del producto por su ID
            instance = self.get_queryset().get(id=id)
            instance.delete()
            return response.Response(data={
                'message': 'Producto eliminado exitosamente'
            }, status=status.HTTP_204_NO_CONTENT)
        except ProductoModel.DoesNotExist:
            return response.Response(data={
                'message': 'Producto no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
