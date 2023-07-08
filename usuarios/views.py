from django.shortcuts import render, redirect
from usuarios.forms.LoginForm import LoginForms
from usuarios.forms.CadastroForm import CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method != 'POST':
        form = LoginForms()
        return render(request, 'usuarios/login.html', {"form": form})

    form = LoginForms(request.POST)

    if not form.is_valid():
        messages.error(request, "Por favor, preencha o formulário corretamente.")
        return redirect('login')
    
    username = form['nome'].value()
    password = form['senha'].value()

    usuario = auth.authenticate(
        request=request,
        username=username,
        password=password
    )

    if not usuario:
        messages.error(request, "Nome ou senha inválido, por favor, tente novamente.")
        return redirect('login')

    auth.login(request, usuario)

    messages.success(request, f"Seja bem vindo {username}.")
    return redirect('index')

def logout(request):
    
    if not request.user.is_authenticated:
        return redirect('login')

    auth.logout(request)
    messages.success(request, "Até logo, volte sempre.")
    return redirect('login')

def cadastro(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method != 'POST':
        form = CadastroForms()
        return render(request, 'usuarios/cadastro.html', {"form": form})

    form = CadastroForms(request.POST)
    if not form.is_valid():
        messages.error(request, "Dados inválidos. Por favor, tente novamente.")
        return render(request, 'usuarios/cadastro.html', {"form": form})

    username = form['nome'].value()
    existe = User.objects.filter(username=username).exists()
    if existe:
        messages.error(request, "Dados inválidos. Por favor, tente novamente.")
        return redirect('cadastro')

    email = form['email'].value()
    password = form['senha'].value()
    usuario = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    usuario.save()

    messages.success(request, "Cadastro efetuado com sucesso.")
    return redirect('login')