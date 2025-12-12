from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import FilmeForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'index.html', {'filmes': filmes,})

class FilmesView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})
# def post(self, request, *args, **kwargs):
class SeriesView(View):
    def get(self, request, *args, **kwargs):
        series = Serie.objects.all()
        return render(request, 'series.html', {'series': series})

class EpisodiosView(View):
    def get(self, request, *args, **kwargs):
        episodios = Episodio.objects.all()
        return render(request, 'episodios.html', {'episodios': episodios})
class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})
class TemporadasView(View):
    def get(self, request, *args, **kwargs):
        temporadas = Temporada.objects.all()
        return render(request, 'temporadas.html', {'temporadas': temporadas})
class ElencoView(View):
    def get(self, request, *args, **kwargs):
        elencos = Elenco.objects.all()
        return render(request, 'elenco.html', {'elencos': elencos})
class AtuacaoView(View):
    def get(self, request, *args, **kwargs):
        atuacoes = Atuacao.objects.all()
        return render(request, 'atuacoes.html', {'atuacoes': atuacoes})

class DeleteFilmeView(View):
    def get(self, request, id, *args, **kwargs):
        filme = Filme.objects.get(id=id)
        filme.delete()
        messages.success(request, 'Filme excluído com sucesso!') # Success message
class EditarFilmeView(View):
    template_name = 'editar_filme.html'
    def get(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(instance=filme)
        return render(request, self.template_name, {'filme': filme, 'form': form})
    def post(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect('editar', id=id) # Redirecionar de volta para a página de edição
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'filme': filme, 'form': form})
