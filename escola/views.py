from escola.models import Estudante, Curso, Matricula, Campus, Predio, Sala
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializers,\
    ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, \
    CampusSerializer, PredioSerializer, SalaSerializer
from rest_framework import viewsets, generics, filters # type: ignore
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle # type: ignore
from escola.throttles import MatriculaAnonRateThrottle
'''
from rest_framework.authentication import BasicAuthentication # type: ignore
'''
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly # type: ignore



class EstudanteViewSet(viewsets.ModelViewSet):
    '''
    essa funcao não é necessaria aqui pois é chamada lá em settings
    authentication_classes = [BasicAuthentication]
    '''
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    # if IsAdminUser() == True:
    #     http_method_names = ["get", "post"]
    http_method_names = ["get", "post"]
    
class CursoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    http_method_names = ["get", "post"]
    
class CampusViewSet(viewsets.ModelViewSet):
    #permission_class = [IsAdminUser]
    queryset = Campus.objects.all().order_by('id')
    serializer_class = CampusSerializer
    http_method_names = ["get", "post"]
    
class PredioViewSet(viewsets.ModelViewSet):
    #permission_class = [IsAdminUser]
    queryset = Predio.objects.all().order_by('id')
    serializer_class = PredioSerializer
    http_method_names = ["get", "post"]

class SalaViewSet(viewsets.ModelViewSet):
    #permission_class = [IsAdminUser]
    queryset = Sala.objects.all().order_by('id')
    serializer_class = SalaSerializer
    http_method_names = ["get", "post"]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializers
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
    