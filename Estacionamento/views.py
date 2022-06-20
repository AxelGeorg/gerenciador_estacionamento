from django.shortcuts import render
from Estacionamento.form import GerenteciaVagasForm
from Estacionamento.models import GerenciaVaga

from mainVagas.models import Vaga


def main(request):
    vagas = Vaga.objects.all()
    data = {'vaga_list': vagas}
    return render(request, 'main.html', data)


def gerenciaVagasCreate(request, pk):
    data = {}
    vaga = Vaga.objects.get(pk=pk)
    gerenciaVaga = GerenciaVaga(vaga)
    data['vaga'] = vaga
    data['form'] = GerenteciaVagasForm(
        request.POST or None, instance=gerenciaVaga)
    return render(request, 'gerenciaVaga_form.html', data)
