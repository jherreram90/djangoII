from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
"""
Cross Site Request Forgery --- exploit (malicioso)
envía al sitio comandos no autorizados "secuestra"
peticiones, sesiones, etc... a través de formularios 
"""
@csrf_exempt
def index(request):
	if request.method=='POST':
		nombre=request.POST.get('nombre')
		email=request.POST.get('email')
		tel=request.POST.get('tel')

		context={
			'nombre':nombre,
			'email':email,
			'tel':tel,
		}
		template=loader.get_template('mostrar.html')
		return HttpResponse(template.render(context,request))

	else:
		template=loader.get_template('index.html')
		return HttpResponse(template.render())



