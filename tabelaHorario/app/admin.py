from django.contrib import admin
from .models import Professor, Sala, Disciplina, Turma, Horario, TabelaHorarios

admin.site.register(Professor)
admin.site.register(Sala)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Horario)
admin.site.register(TabelaHorarios)
