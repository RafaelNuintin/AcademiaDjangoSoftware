from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da cidade")
    uf = models.CharField(max_length = 2, verbose_name = "Uf")

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da ocupação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Area_Saber(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da área")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da pessoa")
    nome_do_pai = models.CharField(max_length = 100, verbose_name = "Nome do pai")
    nome_da_mae = models.CharField(max_length = 100, verbose_name = "Nome da mãe")
    cpf = models.CharField(max_length = 20, verbose_name = "cpf")
    data_nasc = models.DateField(verbose_name = "Data de nascimento")
    email = models.CharField(max_length = 100, verbose_name = "Email")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, verbose_name = "Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE, verbose_name = "Ocupação")

    def __str__(self):
        return f"{self.nome}, {self.cpf}"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Instituicao(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da instituição")
    site = models.CharField(max_length = 100, verbose_name = "Site da instituição")
    telefone = models.CharField(max_length = 20, verbose_name = "Telefone")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, verbose_name = "Cidade")

    def __str__(self):
        return f"{self.nome}, {self.cidade}"
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Curso(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name = "Carga horária total")
    duracao_meses = models.IntegerField(verbose_name = "Duração em meses")
    area_saber = models.ForeignKey(Area_Saber, on_delete = models.CASCADE, verbose_name = "Área do saber")
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE, verbose_name = "Instituição")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"