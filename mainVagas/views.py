from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Vaga


class VagaList(ListView):
    model = Vaga
    fields = '__all__'
    paginate_by = 5

    def get_queryset(self):

        txtStatus = self.request.GET.get('status')
        if txtStatus:
            return Vaga.objects.filter(
                status__icontains=txtStatus)

        return Vaga.objects.all()


class VagaDetail(DetailView):
    model = Vaga
    fields = '__all__'


class VagaCreate(CreateView):
    model = Vaga
    fields = '__all__'
    success_url = reverse_lazy('mainVagas:list')


class VagaUpdate(UpdateView):
    model = Vaga
    fields = '__all__'
    success_url = reverse_lazy('mainVagas:list')


class VagaDelete(DeleteView):
    model = Vaga
    fields = '__all__'
    success_url = reverse_lazy('mainVagas:list')
