from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *


urlpatterns = [
    path('registro', RegistroUsuarioApiView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('perfil', PerfilUsuarioApiView.as_view()),
    path('mostrarCategorias', MostrarCategoriasApiView.as_view()),
    path('mostrarCategoria/<int:id>', MostrarUnaCategoriaApiView.as_view()),
    path('crearCategoria', CrearCategoriaApiView.as_view()),
    path('actualizarCategoria/<int:id>', ActualizarCategoria.as_view()),
    path('eliminarCategoria/<int:id>', EliminarCategoria.as_view())


]
