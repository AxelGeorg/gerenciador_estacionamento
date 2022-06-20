from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Vaga


class VagaList(ListView):
    model = Vaga
    fields = '__all__'


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
