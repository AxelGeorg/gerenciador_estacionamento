from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cliente


class ClienteList(ListView):
    model = Cliente
    fields = '__all__'


class ClienteDetail(DetailView):
    model = Cliente
    fields = '__all__'


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')


class ClienteDelete(DeleteView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')
