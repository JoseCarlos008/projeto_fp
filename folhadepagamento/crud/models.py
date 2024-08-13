from django.db import models

# Create your models here.


class Person (models.Model):
    first_name = models.CharField(max_length=30);
    last_name = models.CharField(max_length=30);
    def __str__(self):
        return self.firstname
    
class Funcionario (models.Model):
    nome = models.CharField(max_length=50);
    salarioBase = models.FloatField(max_length=8);
    nivel = models.IntegerField(max_length=1);
    
    
class Empresa (models.Model):
    nome = models.CharField(max_length=50);
    cnpj = models.CharField(max_length=20);
    telefone = models.CharField(max_length=13);
    email = models.EmailField(max_length=70);
    endereco = models.CharField(max_length=50);
    setores = models.CharField(max_length=20);