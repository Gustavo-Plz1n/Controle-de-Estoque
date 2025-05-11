from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_aquisicao = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Adicione este
    estoque = models.PositiveIntegerField(default=0)
    fornecedor = models.CharField(max_length=100, blank=True)  # Adicione este

    def __str__(self):
        return self.nome
