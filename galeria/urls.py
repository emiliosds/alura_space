from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/', imagem, name = 'imagem'),
]

# pages = ['', 'imagem']
# for page in pages:
    
#     route = ''
#     if page:
#         route = page + '/'
    
#     urlpatterns.append(path())