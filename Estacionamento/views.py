from django.shortcuts import redirect, render
from Estacionamento.form import GerenteciaVagasForm
from Estacionamento.models import GerenciaVaga

from mainVagas.models import EnumStatus, Vaga


def main(request):
    vagas = Vaga.objects.all()
    data = {'vaga_list': vagas}
    return render(request, 'main.html', data)


def gerenciaVagasCreate(request, pk):
    data = {}
    vaga = Vaga.objects.get(pk=pk)
    vaga.status = EnumStatus.ocupado
    gerenciaVaga = GerenciaVaga(vaga=vaga)
    form = GerenteciaVagasForm(
        request.POST or None, instance=gerenciaVaga)

    if form.is_valid():
        form.save()
        vaga.save()
        return redirect('Estacionamento:main')

    data['vaga'] = vaga
    data['form'] = form
    return render(request, 'gerenciaVaga_form.html', data)


def gerenciaVagaList(request):
    gerenciaVaga_list = GerenciaVaga.objects.all()
    form = GerenteciaVagasForm()
    data = {'gerenciaVaga_list': gerenciaVaga_list, 'form': form}
    return render(request, 'gerenciaVaga_list.html', data)


def gerenciaVagasDetail(request, pk):
    data = {}
    gerenciaVaga = GerenciaVaga.objects.get(pk=pk)
    data['gerenciaVaga'] = gerenciaVaga
    return render(request, 'gerenciaVaga_detail.html', data)
