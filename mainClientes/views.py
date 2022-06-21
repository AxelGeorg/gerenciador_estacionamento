from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cliente


class ClienteList(ListView):
    model = Cliente
    fields = '__all__'
    paginate_by = 5

    def get_queryset(self):

        clientes = Cliente.objects.all()

        txtNome = self.request.GET.get('nome')
        if txtNome:
            clientes = clientes.filter(
                nome__icontains=txtNome)

        txtCPF = self.request.GET.get('cpf')
        if txtCPF:
            clientes = clientes.filter(
                cpf__icontains=txtCPF)

        return clientes 


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
