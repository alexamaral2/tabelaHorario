from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField(help_text="Carga horária semanal")

    def __str__(self):
        return self.nome


class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()
    recursos = models.CharField(max_length=255, blank=True, help_text="Ex: Projetor, Quadro interativo")

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField(help_text="Carga horária total da disciplina")

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    numero_alunos = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Horario(models.Model):
    dia_da_semana = models.CharField(max_length=20, choices=[
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    ])
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia_da_semana} ({self.hora_inicio} - {self.hora_fim})"


class TabelaHorarios(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['professor', 'horario'], name='unique_professor_horario'),
            models.UniqueConstraint(fields=['sala', 'horario'], name='unique_sala_horario'),
            models.UniqueConstraint(fields=['turma', 'horario'], name='unique_turma_horario')
        ]

    def __str__(self):
        return f"{self.disciplina.nome} - {self.professor.nome} - {self.sala.nome} ({self.horario})"
