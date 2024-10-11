from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso, \
    CampusViewSet, PredioViewSet, SalaViewSet
from rest_framework import routers # type: ignore

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')
router.register('campus', CampusViewSet, basename='Campus')
router.register('predio', PredioViewSet, basename='Predio')
router.register('sala', SalaViewSet, basename='Sala')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]
