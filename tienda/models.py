from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager
from cloudinary.models import CloudinaryField

# Create your models here.


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.TextField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # cuando queramos ingresar al panel admisnistrativo se le pidira el siguiente atributo al usuario
    USERNAME_FIELD = 'correo'
    # cuando queramos crear un superusuario por la terminal que atributos nos debe solicitar
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'


class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'categorias'


class ProductoModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100,  null=False)
    precio = models.FloatField()
    cantidad = models.SmallIntegerField('Cantidad o Stock', default=1)
    imagen = CloudinaryField('producto', unique=True, null=False)
    disponible = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    categoria = models.ForeignKey(
        to=CategoriaModel, on_delete=models.CASCADE, db_column='categoria_id')

    class Meta:
        db_table = 'productos'
