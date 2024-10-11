from escola.models import Estudante, Curso, Matricula, Campus, Predio, Sala
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializers,\
    ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, \
    CampusSerializer, PredioSerializer, SalaSerializer
from rest_framework import viewsets, generics, filters # type: ignore
'''
from rest_framework.authentication import BasicAuthentication # type: ignore
'''
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly # type: ignore
from django_filters.rest_framework import DjangoFilterBackend # type: ignore


class EstudanteViewSet(viewsets.ModelViewSet):
    '''
    essa funcao não é necessaria aqui pois é chamada lá em settings
    authentication_classes = [BasicAuthentication]
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CampusViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

class PredioViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

class SalaViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializers

class ListaMatriculaEstudante(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
    