from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np

def Alumno1(request):
	template=loader.get_template('alumno1.html')
	Calis=[8,7,7,4]
	Materias=['Mate 1','Progra 1','MVC','Ec. dif.']
	Promedio=np.mean(Calis)
	lista=zip(Materias,Calis) 
	contex={
		'pk':1,
		'Nombre':'Rodrigo Jimenez',
		'Matricula': 123456,
		'Edad':'14',
		'foto':"/static/images/CG1.png",
		'Prom':Promedio,
		'Materias':Materias,
		'lista':lista,
	}
	return HttpResponse(template.render(contex,request))

def Alumno2(request):
	template=loader.get_template('alumno2.html')
	Calis=[6,5,7,10]
	Materias=['Mate 2','POE','MVC','POO']
	Promedio=np.mean(Calis)
	lista=zip(Materias,Calis) 
	contex={
		'pk':2,
		'Nombre':'Juan Gutierrez',
		'Matricula': 987643,
		'Edad':'20',
		'foto':"/static/images/CG2.png",
		'Prom':Promedio,
		'Calis':Calis,
		'Materias':Materias,
		'lista':lista,
	}
	return HttpResponse(template.render(contex,request))
