from django.shortcuts import render
from catalogo.models import Fun

def index(request):
	funciones=Fun.objects.all()
	context={
		'funciones':funciones
	}
	return render(request,'index.html',context)

def detalle(request,pk):
	funcion=Fun.objects.get(pk=pk)
	context={
		'funcion':funcion
	}
	return render(request,'detalle.html',context)


