from django.db import models # type: ignore
from django.core.validators import MinLengthValidator, MaxValueValidator # type: ignore

'''
para implementar CPF real:
    rode o comando
        pip intall django-cpf
    va no settings.py ... adicione esse cara abaixo
        INSTALLED_APPS[
        'cpf_fields',
        ] 
volte para models e importe os campos abaixo

from django.db import models
from cpf_field.models import CPFField

na sua class coloque 
cpf = CPFField('cpf')
'''

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    codigo = models.CharField(max_length=10, validators=[MinLengthValidator(5)])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
    
    def __str__(self):
        return self.codigo

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome

class Campus(models.Model):
    numero_do_campus = models.IntegerField(blank=False, null=False, default=1)
    limite_de_predios = models.IntegerField(blank=False, null=False, default=1)
    #O status diz se o campus está ativado ou desativado
    STATUS = (
        ('L', 'LIBERADO PARA USO'),
        ('N', 'NÃO PODE SER USADO'),
    )
    status_campus = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='L')
    def __str__(self):
        return self.numero_do_campus

class Predio(models.Model):
    numero_do_predio = models.IntegerField(blank=False, null=False, default=1)
    limite_de_salas = models.IntegerField(blank=False, null=False, default=10)
    #O status diz se o predio está ativado ou desativado
    STATUS = (
        ('L', 'LIBERADO PARA USO'),
        ('N', 'NÃO PODE SER USADO'),
    )
    status_predio = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='L')
    def __str__(self):
        return self.numero_do_predio

class Sala(models.Model):
    numero_da_sala = models.IntegerField(blank=False, null=False, default=1)
    limite_de_alunos = models.IntegerField(blank=False, null=False, default=15)
    STATUS = (
        ('L', 'LIBERADO PARA USO'),
        ('N', 'NÃO PODE SER USADO'),
    )
    status_sala = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='L')
    def __str__(self):
        return self.numero_da_sala

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')