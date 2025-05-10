from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime

def home(request):
    # Definindo a variável isActive inicialmente como True
    isActive = True
    
    # Verificando se a requisição é POST e processando a variável 'check'
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)  
        
        # Alterando isActive com base no valor de 'check'
        if check is None:
            isActive = False
        else:
            isActive = True

    # Obtendo a data e hora atual
    date = datetime.datetime.now()  
    
    # Definindo algumas variáveis para o template
    name = "LearnCodeWithDurgesh"
    
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print Pascal\'s triangle'
    ]
    
    student = {
        'student_name': "Rahul",
        'student_college': "ZYZ",
        'student_city': 'LUCKNOW'
    }
    
    # Preparando o contexto a ser passado para o template
    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }
    
    # Passando o contexto para o template
    return render(request, "home.html", data)
def bemvindo(request):
    return render(request, 'emp/bemvindo.html')

def about(request):
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})

def login_view(request):
    if request.method == 'POST':
        # Obtendo dados do formulário de login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificando se os dados estão corretos com o método authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se as credenciais estiverem corretas, faz o login e redireciona
            login(request, user)
            return redirect('/index/')
        else:
            # Se as credenciais estiverem incorretas, envia uma mensagem de erro
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'emp/login.html', {'messages': messages.get_messages(request)})  # Passando as mensagens para o template

    # Caso não tenha sido um POST, apenas renderize o formulário sem erro
    return render(request, 'emp/login.html')

