from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articulo

class ArtList(ListView):
	model=Articulo
	template_name="lista.html"

class ArtDet(DetailView):
	model=Articulo
	template_name="detalle.html"
		
		
