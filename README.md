# PRIMERO:
# CREE MI ENTORNO VIRTUAL : 
 python -m venv entorno_django y lo activamos con entorno_django/Scripts/activate
# SEGUNDO:
# INSTALAMOS DJANGO:
 pip install django
# TERCERO:
# LUEGO DE CREAR NUESTROS ARCHIVOS .gitignore y .env creamos nuestro proyecto:
django-admin startproject mahora
# CUARTO:
# luego de pasarnos a nuestra carpeta de proyecto con cd mahora creamos nuestra aplicacion:
python manage.py startapp tienda
# QUINTO:
# En nuestro archivo settings en INSTALLED_APPS agregamos 'tienda',tambien en DATABASES ingresamos  los parametros para comunicarnos con nuestra base de datos.
# instalamos la libreria pscopg2 para comunicarnos con nuestra BD:
pip install psycopg2
# SEXTO:
# Para que django acepte peticiones http necesitamos instalar django restframework:
pip install djangorestframework
# Para poder hacer nuestras autenticaciones por tokems instalamos:
pip install djangorestframework-simplejwt
# Cree el UsuariModel  en models.py y el archivo auth_manager.py para poder crear un superusuario
# cree mi primera migracion python .\manage.py makemigrations tienda --name "agrege_usuario_model"
# corri la migracion con python .\manage.py migrate tienda
# corri las migraciones faltantes con python .\manage.py migrate     
# para ver sin las migraciones se ejecutaron correctamente utilizamos el comando:
python .\manage.py showmigrations
# creamos nuestro super usuario con el siguiente comando:
python .\manage.py createsuperuser
# creamos nuestra vista RegistroUsuarioApiView y nuestro serializador RegistroUsuarioSerializer
# en nuestro archivo urls.py de nuestra app tienda importamos la vista RegistroUsuarioApiView
# creamos nuestra primera ruta para verla en el postman:
path('registro', RegistroUsuarioApiView.as_view())
# importamos en urls.py de nuestra tienda
from rest_framework_simplejwt.views import TokenObtainPairView
# creamos la ruta login:
 path('login', TokenObtainPairView.as_view())
 



