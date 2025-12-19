from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'index.html', {'cursos': cursos,})
    
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas,})
    
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos,})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes,})

class AreasView(View):
    def get(self, request, *args, **kwargs):
        areas = Area_Saber.objects.all()
        return render(request, 'areas.html', {'areas': areas,})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas,})
    
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas,})
    
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias,})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias,})

class DeleteCursoView(View):
    def get(self, request, id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=id)
        curso.delete()
        messages.success(request, 'Curso excluído com sucesso!')
        return redirect('index')

class EditarCursoView(View):
    def get(self, request, id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=id)
        return render(request, 'editar_curso.html', {'curso': curso})
# Create your views here.
