from django.contrib import admin # type: ignore
from escola.models import Estudante, Curso, Matricula, Campus, Predio, Sala

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome',  'email', 'cpf', 'data_nascimento', 'celular',)
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)
    
admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao',)
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)
    
admin.site.register(Curso, Cursos)

class Campi(admin.ModelAdmin):
    list_display = ('id', 'numero_do_campus', 'limite_de_predios', 'status_campus',)
    list_display_links = ('id', 'numero_do_campus',)
    search_fields = ('numero_do_campus',)
    
admin.site.register(Campus, Campi)

class Predios(admin.ModelAdmin):
    list_display = ('id', 'numero_do_predio', 'limite_de_salas', 'status_predio',)
    list_display_links = ('id', 'numero_do_predio',)
    search_fields = ('numero_do_predio',)
    
admin.site.register(Predio, Predios)

class Salas(admin.ModelAdmin):
    list_display = ('id', 'numero_da_sala', 'limite_de_alunos', 'status_sala',)
    list_display_links = ('id', 'numero_da_sala',)
    search_fields = ('numero_da_sala',)
    
admin.site.register(Sala, Salas)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo',)
    list_display_links = ('id',)
    
admin.site.register(Matricula, Matriculas)
