from django.shortcuts import render
from medico.models import DadosMedico, Especialidades

def home(request):
    if request.method == "GET":
        medico_filtrar = request.GET.get('medico')
        especialidades_filtrar = request.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()
        
        if medico_filtrar: # icontains serve para quando o usuario filtrar pela inicial do nome(ou qualquer letra que esteja no nome do médico), já apareca
            medicos = medicos.filter(nome__icontains = medico_filtrar)
        
        if especialidades_filtrar: # especialidade_id -> serve para procurar pelo id da especialidade, especialidade_id__in -> serve para buscar todas especialidades por id, ou seja pega varios id's
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)
            
        
        especialidades = Especialidades.objects.all()
        return render(request, 'home.html', {'medicos':medicos,
                                             'especialidades':especialidades})