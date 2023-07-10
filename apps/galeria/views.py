from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada = True)
    return render(request, 'galeria/index.html', { 'cards' : fotografias })

def cadastrar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem cadastrada com sucesso.')
            return redirect('index')

    form = FotografiaForms()
    return render(request, 'galeria/cadastrar.html', { 'form' : form })

def visualizar(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/visualizar.html', { 'fotografia' : fotografia })

def editar(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')
    
    fotografia = Fotografia.objects.get(id = id)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance = fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso.')
            return redirect('galeria/visualizar', id = fotografia.id)

    form = FotografiaForms(instance = fotografia)
    return render(request, 'galeria/editar.html', { 'form' : form, 'id' : fotografia.id })

def excluir(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    fotografia = Fotografia.objects.filter(id = id).first()
    if not fotografia:
        messages.error(request, 'Fotografia não encontrada.')
        return redirect('index')

    exclusao = fotografia.delete()
    if exclusao:
        messages.success(request, 'Fotografia excluida com sucesso.')
        return redirect('index')
    
    messages.error(request, 'Erro durante o processo de exclusão da fotografia.')
    return redirect('index')

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = Fotografia.objects.order_by('-data_fotografia').filter(nome__icontains = nome_a_buscar)

    return render(request, 'galeria/index.html', { 'cards' : fotografias })

def filtrar(request, categoria):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado.')
        return redirect('usuario/login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada = True, categoria = categoria)
    return render(request, 'galeria/index.html', { 'cards' : fotografias })