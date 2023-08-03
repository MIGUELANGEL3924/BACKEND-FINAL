from rest_framework.permissions import BasePermission


class SoloAdministrador(BasePermission):
    def has_permission(self, request, view):
        tipoUsuario = request.user.tipoUsuario
        if tipoUsuario == 'ADMIN':
            return True
        else:
            return False
