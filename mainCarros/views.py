from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Carro


class CarroList(ListView):
    model = Carro
    fields = '__all__'


class CarroDetail(DetailView):
    model = Carro
    fields = '__all__'


class CarroCreate(CreateView):
    model = Carro
    fields = '__all__'
    success_url = reverse_lazy('mainCarros:list')


class CarroUpdate(UpdateView):
    model = Carro
    fields = '__all__'
    success_url = reverse_lazy('mainCarros:list')


class CarroDelete(DeleteView):
    model = Carro
    fields = '__all__'
    success_url = reverse_lazy('mainCarros:list')
