from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from escola.views import EstudanteViewSet,CursoViewSet
from rest_framework import routers # type: ignore

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
