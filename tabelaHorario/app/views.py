from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Professor, Sala, Disciplina, Turma, Horario, TabelaHorarios

def index(request):
    return render(request, 'index.html')

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor_list.html'
    context_object_name = 'professores'

class ProfessorCreateView(CreateView):
    model = Professor
    template_name = 'professor_form.html'
    fields = ['nome', 'carga_horaria']
    success_url = reverse_lazy('professor_list')

class ProfessorUpdateView(UpdateView):
    model = Professor
    template_name = 'professor_form.html'
    fields = ['nome', 'carga_horaria']
    success_url = reverse_lazy('professor_list')

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor_confirm_delete.html'
    success_url = reverse_lazy('professor_list')

class SalaListView(ListView):
    model = Sala
    template_name = 'sala_list.html'
    context_object_name = 'salas'

class SalaCreateView(CreateView):
    model = Sala
    template_name = 'sala_form.html'
    fields = ['nome', 'capacidade', 'recursos']
    success_url = reverse_lazy('sala_list')

class SalaUpdateView(UpdateView):
    model = Sala
    template_name = 'sala_form.html'
    fields = ['nome', 'capacidade', 'recursos']
    success_url = reverse_lazy('sala_list')

class SalaDeleteView(DeleteView):
    model = Sala
    template_name = 'sala_confirm_delete.html'
    success_url = reverse_lazy('sala_list')

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'disciplina_list.html'
    context_object_name = 'disciplinas'

class DisciplinaCreateView(CreateView):
    model = Disciplina
    template_name = 'disciplina_form.html'
    fields = ['nome', 'carga_horaria']
    success_url = reverse_lazy('disciplina_list')

class DisciplinaUpdateView(UpdateView):
    model = Disciplina
    template_name = 'disciplina_form.html'
    fields = ['nome', 'carga_horaria']
    success_url = reverse_lazy('disciplina_list')

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    template_name = 'disciplina_confirm_delete.html'
    success_url = reverse_lazy('disciplina_list')

class TurmaListView(ListView):
    model = Turma
    template_name = 'turma_list.html'
    context_object_name = 'turmas'

class TurmaCreateView(CreateView):
    model = Turma
    template_name = 'turma_form.html'
    fields = ['nome', 'numero_alunos']
    success_url = reverse_lazy('turma_list')

class TurmaUpdateView(UpdateView):
    model = Turma
    template_name = 'turma_form.html'
    fields = ['nome', 'numero_alunos']
    success_url = reverse_lazy('turma_list')

class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = 'turma_confirm_delete.html'
    success_url = reverse_lazy('turma_list')

class HorarioListView(ListView):
    model = Horario
    template_name = 'horario_list.html'
    context_object_name = 'horarios'

class HorarioCreateView(CreateView):
    model = Horario
    template_name = 'horario_form.html'
    fields = ['dia_da_semana', 'hora_inicio', 'hora_fim']
    success_url = reverse_lazy('horario_list')

class HorarioUpdateView(UpdateView):
    model = Horario
    template_name = 'horario_form.html'
    fields = ['dia_da_semana', 'hora_inicio', 'hora_fim']
    success_url = reverse_lazy('horario_list')

class HorarioDeleteView(DeleteView):
    model = Horario
    template_name = 'horario_confirm_delete.html'
    success_url = reverse_lazy('horario_list')

class TabelaHorariosListView(ListView):
    model = TabelaHorarios
    template_name = 'tabelahorarios_list.html'
    context_object_name = 'tabela_horario'

class TabelaHorariosCreateView(CreateView):
    model = TabelaHorarios
    template_name = 'tabelahorarios_form.html'
    fields = ['professor', 'sala', 'disciplina', 'turma', 'horario']
    success_url = reverse_lazy('tabela_horario_list')

class TabelaHorariosUpdateView(UpdateView):
    model = TabelaHorarios
    template_name = 'tabelahorarios_form.html'
    fields = ['professor', 'sala', 'disciplina', 'turma', 'horario']
    success_url = reverse_lazy('tabela_horario_list')

class TabelaHorariosDeleteView(DeleteView):
    model = TabelaHorarios
    template_name = 'tabelahorarios_confirm_delete.html'
    success_url = reverse_lazy('tabela_horario_list')
