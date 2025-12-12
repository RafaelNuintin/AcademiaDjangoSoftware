from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do gênero")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Episodio(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do episódio")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Episódio"
        verbose_name_plural = "Episódios"

class Temporada(models.Model):
    temporada = models.IntegerField(verbose_name = "Temporada")

    def __str__(self):
        return f"{self.temporada}º temporada"

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

class Continente(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Continente"
        verbose_name_plural = "Continentes"

class Pais(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do país")
    continente = models.ForeignKey(Continente, on_delete = models.CASCADE, verbose_name = "Continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

class Elenco(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome")
    site = models.CharField(max_length = 100, verbose_name = "Site")
    insta = models.CharField(max_length = 100, verbose_name = "Instagram")
    face = models.CharField(max_length = 100, verbose_name = "Facebook")
    nacionalidade = models.CharField(max_length = 100, verbose_name = "Nacionalidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Elenco"
        verbose_name_plural = "Elencos"

class Filme(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do filme")
    duracao = models.IntegerField(verbose_name = "Duração do filme")
    sinopse = models.CharField(max_length = 1000, verbose_name = "Sinopse")
    site_oficial = models.CharField(max_length = 100, verbose_name = "Site do filme")
    data_lancamento = models.DateField(verbose_name = "Data de lançamento")
    nota_avaliacao = models.FloatField(verbose_name = "Nota da avaliação")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, verbose_name = "Gênero")
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name = "País")
    diretor = models.ForeignKey(Elenco, on_delete = models.CASCADE, verbose_name = "Diretor")

    def __str__(self):
        return f"{self.nome}, {self.data_lancamento}"
    
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

class Atuacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, verbose_name = "Filme")
    ator = models.ForeignKey(Elenco, on_delete=models.CASCADE, verbose_name = "Ator")

    def __str__(self):
        return f"{self.ator}, {self.filme}"

    class Meta:
        verbose_name = "Atuação"
        verbose_name_plural = "Atuações"

class Serie(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da série")
    temporadas = models.IntegerField(verbose_name = "Temporadas da série")
    sinopse = models.CharField(max_length = 1000, verbose_name = "Sinopse")
    site_oficial = models.CharField(max_length = 100, verbose_name = "Site da série")
    data_lancamento = models.DateField(verbose_name = "Data de lançamento")
    nota_avaliacao = models.FloatField(verbose_name = "Nota da avaliação")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, verbose_name = "Gênero")
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name = "País")
    diretor = models.ForeignKey(Elenco, on_delete = models.CASCADE, verbose_name = "Elenco")

    def __str__(self):
        return f"{self.nome}, {self.data_lancamento}"

    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Séries"

class EpisodiosSerie(models.Model):
    serie = models.ForeignKey(Serie, on_delete = models.CASCADE, verbose_name = "Nome da série")
    temporada = models.ForeignKey(Temporada, on_delete = models.CASCADE, verbose_name = "Temporada da série")
    episodio = models.ForeignKey(Episodio, on_delete = models.CASCADE, verbose_name = "Episódio da série")
    duracao = models.IntegerField(verbose_name = "Duração")
    data_disponibilizacao = models.DateField(verbose_name = "Data de disponibilização")

    def __str__(self):
        return f"{self.episodio}, {self.temporada}, {self.serie}"

    class Meta:
        verbose_name = "Episódio de série"
        verbose_name_plural = "Episódios de série"