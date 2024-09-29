from django.urls import path
from .views import (TabelaHorariosListView, TabelaHorariosCreateView, TabelaHorariosUpdateView, 
                    TabelaHorariosDeleteView, ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView,
                    SalaListView, SalaCreateView, SalaUpdateView, SalaDeleteView,
                    DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView,
                    TurmaListView, TurmaCreateView, TurmaUpdateView, TurmaDeleteView,
                    HorarioListView, HorarioCreateView, HorarioUpdateView, HorarioDeleteView)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabelahorario/', TabelaHorariosListView.as_view(), name='tabela_horarios_list'),
    path('create/', TabelaHorariosCreateView.as_view(), name='tabela_horarios_create'),
    path('update/<int:pk>/', TabelaHorariosUpdateView.as_view(), name='tabela_horarios_update'),
    path('delete/<int:pk>/', TabelaHorariosDeleteView.as_view(), name='tabela_horarios_delete'),
    
    path('professor/', ProfessorListView.as_view(), name='professor_list'),
    path('professor/create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('professor/update/<int:pk>/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('professor/delete/<int:pk>/', ProfessorDeleteView.as_view(), name='professor_delete'),

    path('sala/', SalaListView.as_view(), name='sala_list'),
    path('sala/create/', SalaCreateView.as_view(), name='sala_create'),
    path('sala/update/<int:pk>/', SalaUpdateView.as_view(), name='sala_update'),
    path('sala/delete/<int:pk>/', SalaDeleteView.as_view(), name='sala_delete'),

    path('disciplina/', DisciplinaListView.as_view(), name='disciplina_list'),
    path('disciplina/create/', DisciplinaCreateView.as_view(), name='disciplina_create'),
    path('disciplina/update/<int:pk>/', DisciplinaUpdateView.as_view(), name='disciplina_update'),
    path('disciplina/delete/<int:pk>/', DisciplinaDeleteView.as_view(), name='disciplina_delete'),

    path('turma/', TurmaListView.as_view(), name='turma_list'),
    path('turma/create/', TurmaCreateView.as_view(), name='turma_create'),
    path('turma/update/<int:pk>/', TurmaUpdateView.as_view(), name='turma_update'),
    path('turma/delete/<int:pk>/', TurmaDeleteView.as_view(), name='turma_delete'),
    
    path('horario/', HorarioListView.as_view(), name='horario_list'),
    path('horario/create/', HorarioCreateView.as_view(), name='horario_create'),
    path('horario/update/<int:pk>/', HorarioUpdateView.as_view(), name='horario_update'),
    path('horario/delete/<int:pk>/', HorarioDeleteView.as_view(), name='horario_delete'),
    
    path('tabelahorarios/', TabelaHorariosListView.as_view(), name='tabela_horario_list'),
    path('tabelahorarios/create/', TabelaHorariosCreateView.as_view(), name='tabela_horario_create'),
    path('tabelahorarios/<int:pk>/edit/', TabelaHorariosUpdateView.as_view(), name='tabela_horario_update'),
    path('tabelahorarios/<int:pk>/delete/', TabelaHorariosDeleteView.as_view(), name='tabela_horario_delete'),
]
