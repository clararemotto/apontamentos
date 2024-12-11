from django.shortcuts import render, redirect
# from .models import Activity
from django.shortcuts import render
from .models import Cliente, Atividade

def index(request):
    # Pega o ID do cliente enviado pelo formulário
    client_id = request.GET.get('client_name')
    
    # Busca as atividades com base no ID do cliente
    if client_id:
        # Filtra as atividades pelo ID do cliente
        atividades = Atividade.objects.filter(cliente__id=client_id)
    else:
        # Se nenhum filtro for aplicado, traz todas as atividades
        atividades = Atividade.objects.all()
    
    # Passa as atividades para o template
    context = {
        "atividades": atividades,
        "clientes": Cliente.objects.all()
    }
    
    return render(request, 'activity/index.html', context)



def add_activity(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        id_company = request.POST.get('id_company')
        active = request.POST.get('active') == 'Sim'  # Converte para booleano
        client_id = request.POST.get('client_id')
        id_project = request.POST.get('id_project')
        id_user = request.POST.get('id_user')
        activity_name = request.POST.get('activity_name')
        subactivity_name = request.POST.get('subactivity_name')
        hour_in = request.POST.get('hour_in')
        hour_out = request.POST.get('hour_out')
        desc_activity = request.POST.get('desc_activity')
        hour_act = request.POST.get('hour_act')
        hour_add = request.POST.get('hour_add')

        # Cria um novo registro no banco de dados
        Activity.objects.create(
            id_company=id_company,
            active=active,
            client_id=client_id,
            id_project=id_project,
            id_user=id_user,
            activity_name=activity_name,
            subactivity_name=subactivity_name,
            hour_in=hour_in,
            hour_out=hour_out,
            desc_activity=desc_activity,
            hour_act=hour_act,
            hour_add=hour_add,
        )

        # Redireciona para a página de confirmação ou lista
        return redirect('add')  # Substitua 'add' pelo nome do path desejado

    # Renderiza o formulário vazio no caso de GET
    return render(request, 'activity/add_activity.html')
