from django.shortcuts import render
from .models import Pelicula, Director
from django.views import generic

def index(request):
	peliculas=Pelicula.objects.all().count()
	directores=Director.objects.all().count()
	context={
		'peliculas':peliculas,
		'directores':directores,
	}
	return render(request,'index.html',context)

class PelisListView(generic.ListView):
	model=Pelicula
	context_object_name = 'pelis'
	template_name='peliculas_list.html'

class PelisDetailView(generic.DetailView):
	model=Pelicula
	context_object_name='peli'
	template_name='peliculas_detalle.html'

