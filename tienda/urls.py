from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *


urlpatterns = [
    path('registro', RegistroUsuarioApiView.as_view())
]
