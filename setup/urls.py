from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from escola.views import estudantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudantes/', estudantes)
]
