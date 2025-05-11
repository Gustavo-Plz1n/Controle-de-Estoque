from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime
# from .models import Produto   # descomente se já houver o modelo

# -------------------------------
# Páginas genéricas / exemplo
# -------------------------------

def home(request):
    # Flag de exibição
    isActive = True

    if request.method == 'POST':
        check = request.POST.get('check')
        isActive = bool(check)

    data = {
        'date': datetime.datetime.now(),
        'isActive': isActive,
        'name': 'LearnCodeWithDurgesh',
        'list_of_programs': [
            'WAP to check even or odd',
            'WAP to check prime number',
            'WAP to print all prime numbers from 1 to 100',
            'WAP to print Pascal\'s triangle',
        ],
        'student_data': {
            'student_name': 'Rahul',
            'student_college': 'ZYZ',
            'student_city': 'LUCKNOW',
        },
    }
    return render(request, 'home.html', data)


def bemvindo(request):
    return render(request, 'emp/bemvindo.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


# -------------------------------
# CRUD de Produto
# -------------------------------

def add_produto(request):
    if request.method == 'POST':
        # salvar produto novo ou adicionar quantidade…
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('add_produto')          # nome da URL de cadastro
    return render(request, 'emp/add_produto.html')


def update_produto(request, produto_id):
    """
    Atualiza um produto existente.
    Após atualização, redireciona para 'allprod' com mensagem.
    """
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.nome            = request.POST.get('nome')
        produto.descricao       = request.POST.get('descricao')
        produto.estoque         = request.POST.get('estoque')
        produto.preco_aquisicao = request.POST.get('preco_aquisicao')
        produto.preco           = request.POST.get('preco')
        produto.fornecedor      = request.POST.get('fornecedor')
        produto.save()

        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('allprod')

    return render(request, 'emp/update_produto.html', {'produto': produto})


# -------------------------------
# Autenticação
# -------------------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/bemvindo/')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            # Basta renderizar — o bloco {% if messages %} do template cuida da exibição
            return render(request, 'emp/login.html')

    return render(request, 'emp/login.html')
