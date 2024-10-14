import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Estudante, Curso, Matricula

periodos = ['M', 'V', 'N']
estudantes = Estudante.objects.all()
cursos = Curso.objects.all()

def criar_matricula():
    for estudante in estudantes:
        curso = random.choice(cursos)
        periodo = random.choice(periodos)
        Matricula.objects.create(estudante=estudante, curso=curso, periodo=periodo)
criar_matricula()