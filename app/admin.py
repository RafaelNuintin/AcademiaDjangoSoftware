from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class AlunoInline(admin.TabularInline):
    model = Aluno
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AvaliacaoInline]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AlunoInline]

class UfAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CidadeInline]

admin.site.register(Pessoa)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Area_Saber, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Periodo)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Cidade)
admin.site.register(Ocorrencia)
admin.site.register(Uf, UfAdmin)
