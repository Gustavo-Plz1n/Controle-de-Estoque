from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from django.contrib import messages
from . import models
from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})
@login_required
def getProd(request):
    produtos = models.Produto.objects.all()
    return render(request, "emp/allProd.html", {'produtos': produtos})
@login_required
def emp_busca(request):
    emps=Emp.objects.all()
    return render(request,"emp/busca_Produtos.html",{'emps':emps})
@login_required
def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

@login_required
def add_produto(request):
    if request.method == "POST":
        tipo = request.POST.get("tipo_produto")

        if tipo == "novo":
            nome = request.POST.get("nome")
            descricao = request.POST.get("descricao", "")
            quantidade = request.POST.get("quantidade")
            preco_aquisicao = request.POST.get("preco_aquisicao")
            preco_venda = request.POST.get("preco_venda")
            fornecedor = request.POST.get("fornecedor", "")

            # Validação mínima
            if not nome or not preco_venda or not quantidade:
                messages.error(request, "Nome, quantidade e preço de venda são obrigatórios.")
                return render(request, "emp/add_produto.html")

            try:
                quantidade = int(quantidade)
                preco_aquisicao = Decimal(preco_aquisicao) if preco_aquisicao else Decimal("0.00")
                preco_venda = Decimal(preco_venda)

                produto = models.Produto(
                    nome=nome,
                    descricao=descricao,
                    preco=preco_venda,
                    preco_aquisicao=preco_aquisicao,
                    estoque=quantidade,
                    fornecedor=fornecedor
                )
                produto.save()
                messages.success(request, "Produto novo cadastrado com sucesso.")
                return redirect("/emp/check-prod/")

            except (ValueError, InvalidOperation):
                messages.error(request, "Dados numéricos inválidos para quantidade ou preço.")

        elif tipo == "existente":
            nome_existente = request.POST.get("nome_existente")
            quantidade_existente = request.POST.get("quantidade_existente")

            if not nome_existente or not quantidade_existente:
                messages.error(request, "Nome do produto e quantidade são obrigatórios.")
                return render(request, "emp/add_produto.html")

            try:
                quantidade_existente = int(quantidade_existente)

                produto = models.Produto.objects.filter(nome=nome_existente).first()
                if produto:
                    produto.estoque += quantidade_existente
                    produto.save()
                    messages.success(request, "Estoque do produto atualizado com sucesso.")
                    return redirect("/emp/check-prod/")
                else:
                    messages.error(request, "Produto não encontrado.")

            except ValueError:
                messages.error(request, "Quantidade deve ser um número inteiro válido.")

    return render(request, "emp/add_produto.html")
@login_required
def update_produto(request, produto_id):
    produto = get_object_or_404(models.Produto, pk=produto_id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao", "")
        estoque = request.POST.get("estoque")
        preco_aquisicao = request.POST.get("preco_aquisicao")
        preco = request.POST.get("preco")
        fornecedor = request.POST.get("fornecedor", "")

        try:
            produto.nome = nome
            produto.descricao = descricao
            produto.estoque = int(estoque)
            produto.preco_aquisicao = float(preco_aquisicao)
            produto.preco = float(preco)
            produto.fornecedor = fornecedor
            produto.save()

            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("/emp/check-prod/")  # redireciona para a página de listagem
        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao atualizar o produto: {str(e)}")

    return render(request, "emp/update_produto.html", {"produto": produto})
@login_required
def delete_produto(request, produto_id):
    try:
        produto = models.Produto.objects.get(pk=produto_id)
        produto.delete()
        messages.success(request, "Produto deletado com sucesso.")
    except models.Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado.")
    return redirect("/emp/check-prod/")

@login_required
def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")
@login_required
def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })
@login_required
def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")

@login_required
def buscar_produto_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()

        if not query:
            messages.error(request, "Por favor, insira um termo de busca.")
            return render(request, 'emp/buscar_produto.html')

        # Gera expressão com letras na ordem (ex: abc -> a.*b.*c)
        import re
        pattern = '.*'.join(map(re.escape, query))
        
        produtos = models.Produto.objects.filter(nome__iregex=pattern)

        if not produtos.exists():
            messages.info(request, "Nenhum produto encontrado com esse critério.")

        return render(request, 'emp/buscar_produto.html', {
            'produtos': produtos,
            'query': query,
            'messages': messages.get_messages(request)
        })

    # Se for GET, apenas mostra o formulário
    return render(request, 'emp/buscar_produto.html')
