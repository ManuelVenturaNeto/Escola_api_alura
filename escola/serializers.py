from rest_framework import serializers # type: ignore
from escola.models import Estudante,Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        filter = '__all__'