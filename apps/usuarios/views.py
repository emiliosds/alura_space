from django.shortcuts import render, redirect
from apps.usuarios.forms.LoginForm import LoginForms
from apps.usuarios.forms.CadastroForm import CadastrarForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method != 'POST':
        form = LoginForms()
        return render(request, 'usuarios/login.html', { 'form' : form })

    form = LoginForms(request.POST)

    if not form.is_valid():
        messages.error(request, 'Por favor, preencha o formulário corretamente.')
        return redirect('usuario/login')
    
    username = form['nome'].value()
    password = form['senha'].value()

    usuario = auth.authenticate(
        request=request,
        username=username,
        password=password
    )

    if not usuario:
        messages.error(request, 'Nome ou senha inválido, por favor, tente novamente.')
        return redirect('usuario/login')

    auth.login(request, usuario)

    messages.success(request, f'Seja bem vindo {username}.')
    return redirect('index')

def logout(request):    
    if not request.user.is_authenticated:
        return redirect('usuario/login')

    auth.logout(request)
    messages.success(request, 'Até logo, volte sempre.')
    return redirect('usuario/login')

def cadastrar(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method != 'POST':
        form = CadastrarForms()
        return render(request, 'usuarios/cadastrar.html', { 'form' : form })

    form = CadastrarForms(request.POST)
    if not form.is_valid():
        messages.error(request, 'Dados inválidos. Por favor, tente novamente.')
        return render(request, 'usuarios/cadastrar.html', { 'form' : form })

    username = form['nome'].value()
    existe = User.objects.filter(username = username).exists()
    if existe:
        messages.error(request, 'Dados inválidos. Por favor, tente novamente.')
        return redirect('usuario/cadastrar')

    email = form['email'].value()
    password = form['senha'].value()
    usuario = User.objects.create_user(
        username = username,
        email = email,
        password = password
    )
    usuario.save()

    messages.success(request, 'Cadastro efetuado com sucesso.')
    return redirect('usuario/login')