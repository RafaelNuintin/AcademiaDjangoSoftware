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

class Periodo(models.Model):
    periodo = models.IntegerField(verbose_name = "Período de Curso")

    def __str__(self):
        return self.periodo
    
    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"

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

class Disciplina(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Disciplina")
    area_saber = models.ForeignKey(Area_Saber, on_delete = models.CASCADE, verbose_name = "Área do Saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

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

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE, verbose_name = "Instituição")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa")
    data_inicio = models.DateField(verbose_name = "Data de Início")
    data_previsao_termino = models.DateField(verbose_name = "Data de Previsão de Término")

    def __str__(self):
        return f"{self.curso}, {self.instituicao}, {self.pessoa}"
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length = 500, verbose_name = "Descrição")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Disciplina")

    def __str__(self):
        return f"{self.curso}, {self.disciplina}"
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do tipo")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "TipoAvaliação"
        verbose_name_plural = "TiposAvaliações"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa")
    numero_faltas = models.IntegerField(verbose_name = "Número de faltas")

    def __str__(self):
        return f"{self.pessoa}, {self.disciplina}"
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Turma(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da turma")
    turno = models.CharField(max_length = 100, verbose_name = "Turno")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length = 500, verbose_name = "Descrição")
    data = models.DateField(verbose_name = "Data")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa")

    def __str__(self):
        return f"{self.pessoa}, {self.data}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class Disciplina_Curso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Disciplina")
    carga_horaria = models.IntegerField(verbose_name = "Carga horária")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    periodo = models.ForeignKey(Periodo, on_delete = models.CASCADE, verbose_name = "Período")

    def __str__(self):
        return f"{self.disciplina}, {self.curso}"
    
    class Meta:
        verbose_name = "DisciplinaCurso"
        verbose_name_plural = "DisciplinasCursos"