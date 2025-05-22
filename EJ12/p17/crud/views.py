from django.shortcuts import render
from .models import ListaR
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class Listar(ListView):
	model=ListaR
	template_name='list.html'
	context_object_name='listas'

class VistaInd(DetailView):
	model=ListaR
	template_name='detalle.html'
	context_object_name='cancion'

class Crear(CreateView):
	model=ListaR
	template_name='crear.html'
	fields=('nombre','artista','album')
	success_url=reverse_lazy('list')#Regresa al listado

class Actualizar(UpdateView):
	model=ListaR
	template_name='actualiza.html'
	context_object_name='cancion'
	fields=('nombre','artista','album','duracion')

	def get_success_url(self):
		return reverse_lazy('detalle',kwargs={'pk':self.object.id})

class Eliminar(DeleteView):
	model=ListaR
	template_name='elimina.html'
	success_url=reverse_lazy('list')
	
		











		
		


