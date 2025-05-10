from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticando o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se o usuário for autenticado, faz login e redireciona para a página principal
            login(request, user)
            return redirect('/index/')  # Redireciona para a página principal (ou onde você desejar)
        else:
            # Caso o login falhe, renderize o login novamente com uma mensagem de erro
            return render(request, 'emp/login.html', {'error': 'Invalid username or password'})

    return render(request, 'emp/login.html')
