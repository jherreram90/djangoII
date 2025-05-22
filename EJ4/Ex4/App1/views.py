from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def v1a1(request):
	template=loader.get_template('v1a1.html')
	operacion=3*2
	context={
		'Vista':'Vista1',
		'App':'Aplicación 1',
		'Op':operacion,
	}
	return HttpResponse(template.render(context,request))