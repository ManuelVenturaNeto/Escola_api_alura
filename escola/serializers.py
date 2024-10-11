from rest_framework import serializers # type: ignore
from escola.models import Estudante, Curso, Matricula, Campus, Predio, Sala
from escola.validators import nome_invalido, cpf_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
    
    #com o metodo unico ele avalia um de cada vez... se fez separado ele ja notifica para o usuario todos os erros de uma vez.
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor valido!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras!'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo: 12 12345-1234 (repeitando traços e espaços)!'})
        return dados
    
    
    '''
    #agora a validadação está vindo de validators mas ela poderia estar aqui:
    #tudo dentro da classe meta da classe que vc quer validar
    #uma forma de validar todos juntos com uma def:
    def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos!'})
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'nome':'O nome só pode ter letras!'})
        if len(dados['celular']) != 14:
            raise serializers.ValidationError({'celular':'O celular precisa ter 14 dígitos!'})
        return serializers.ValidationError
    ---------------------------------------------------------------------------------------------------
    #outra forma possivel de validar com uma def para cada um:    
    def validate_cpf(self,cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos!')
        return cpf
    def validate_nome(self,nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome só pode ter letras!')
        return nome
    def validate(self,celular):
        if len(celular) != 14:
            raise serializers.ValidationError('O celular precisa ter 14 dígitos!')
        return celular
    '''
    
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'
    def validate_numero_do_campus(self, numero_do_campus):
        #Aqui diz quantos campus a universidade tem atualmente
        #Hoje ela tem 7 campus, pois tinha 8 mas vendeu o 3
        if numero_do_campus < 1 or numero_do_campus > 8 or numero_do_campus == 3:
            raise serializers.ValidationError('O campus que você especificou não existe!')
        return numero_do_campus
    def validate_status_campus(self, status_campus):
        if status_campus != 'L':
            raise serializers.ValidationError('O campus não está liberado para uso!')
        return status_campus
        
class PredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predio
        fields = '__all__'
    def validate_numero_do_predio(self, numero_do_predio):
        if numero_do_predio < 1 or numero_do_predio > Campus.limite_de_predios:
            raise serializers.ValidationError('O predio que você busca não existe no campus que voce está cadastrando!')
        return numero_do_predio
    def validate_status_predio(self, status_predio):
        if status_predio != 'L':
            raise serializers.ValidationError('O predio não está liberado para uso!')
        return status_predio
    
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
    def validate_numero_da_sala(self, numero_da_sala):
        if numero_da_sala < 1 or numero_da_sala > Predio.limite_de_salas:
            raise serializers.ValidationError('A sala que você busca não existe no predio que você está cadastrando!')
        return numero_da_sala
    def validate_status_sala(self, status_sala):
        if status_sala != 'L':
            raise serializers.ValidationError('A sala não está liberada para uso!')
        return status_sala

        
class MatriculaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []    
        
        
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso_descricao = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso_descricao', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
    
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome',]