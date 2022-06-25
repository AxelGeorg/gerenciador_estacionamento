from django.forms import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import date
from datetime import datetime

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


def verificar_data(data):
    if data:
        data = datetime.strptime(data, "%d/%m/%Y")
        today = date.today()
        if (today.year - data.year - ((today.month, today.day) < (data.month, data.day))) >= 18:
            return True
        else:
            return False

    return True


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')

    def form_valid(self, form):
        if verificar_data(form.data['data_nascimento']) == False:
            form.add_error('data_nascimento', ValidationError(
                f"Cliente não pode ser menor de idade."))
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')


class ClienteDelete(DeleteView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('mainClientes:list')
