from django.urls import path
from apps.usuarios.views import login, logout, cadastrar

urlpatterns = [
    path('usuario/login', login, name = 'usuario/login'),
    path('usuario/logout', logout, name = 'usuario/logout'),
    path('usuario/cadastrar', cadastrar, name = 'usuario/cadastrar')
]