from django.http import HttpResponse
from django.shortcuts import render
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

def about(request):
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})

def login_view(request):
    return render(request, 'emp/login.html')
