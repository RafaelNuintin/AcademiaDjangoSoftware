from django.contrib import admin
from .models import *

admin.site.register(Instituicao)
admin.site.register(Area_Saber)
admin.site.register(Curso)
admin.site.register(Periodo)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Cidade)
admin.site.register(Ocorrencia)

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Pessoa)
admin.site.register(Ocupacao, OcupacaoAdmin)
