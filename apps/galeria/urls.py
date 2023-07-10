from django.urls import path
from apps.galeria.views import index, visualizar, buscar, cadastrar, editar, excluir, filtrar

urlpatterns = [
    path('', index, name = 'index'),
    path('galeria/visualizar/<int:id>', visualizar, name = 'galeria/visualizar'),
    path('galeria/buscar', buscar, name = 'galeria/buscar'),
    path('galeria/cadastrar', cadastrar, name = 'galeria/cadastrar'),
    path('galeria/editar/<int:id>', editar, name = 'galeria/editar'),
    path('galeria/excluir/<int:id>', excluir, name = 'galeria/excluir'),
    path('galeria/filtrar/<str:categoria>', filtrar, name = 'galeria/filtrar')
]