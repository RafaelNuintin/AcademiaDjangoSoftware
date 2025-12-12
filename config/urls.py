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
    path('filmes/', FilmesView.as_view(), name='filmes'),
path('series/', SeriesView.as_view(), name='series'),
path('episodios/', EpisodiosView.as_view(), name='episodios'),
path('generos/', GenerosView.as_view(), name='generos'),
path('temporadas/', TemporadasView.as_view(), name='temporadas'),
path('elencos/', ElencoView.as_view(), name='elencos'),
path('atuacoes/', AtuacaoView.as_view(), name='atuacoes'),
path('delete/<int:id>/', DeleteFilmeView.as_view(), name='delete'),
path('editar/<int:id>/', EditarFilmeView.as_view(), name='editar'),
path('', IndexView.as_view(), name='index'),
]
