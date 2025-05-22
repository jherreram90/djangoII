from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def v1a2(request):
	template=loader.get_template('v1a1.html')
	operacion=3+7
	context={
		'Vista':'Vista 2',
		'App':'Aplicación 2',
		'Op':operacion,
	}
	return HttpResponse(template.render(context,request))