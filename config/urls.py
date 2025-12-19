"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('areas/', AreasView.as_view(), name='areas'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('delete/<int:id>/', DeleteCursoView.as_view(), name='delete'),
    path('editar/<int:id>/', EditarCursoView.as_view(), name='editar'),
]
