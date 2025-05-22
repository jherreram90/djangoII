from django.shortcuts import render
from django.template import loader
from django.template.loader import get_template
from Html2Pdf import utils
from django.http import HttpResponse

def index(request):
	template=loader.get_template('index.html')
	a=1
	b=2
	suma=a+b
	context={
		'Var1':'Esto es un ejemplo de cómo crear pdfs a partir de vistas',
		'Var2':123,
		'Suma':suma,
	}
	return HttpResponse(template.render(context,request))

def GenPdf(request):
	a=1
	b=2
	suma=a+b
	context={
		'Var1':'Esto es un ejemplo de cómo crear pdfs a partir de vistas',
		'Var2':123,
		'Suma':suma,
	}
	pdf=utils.render_to_pdf('index.html',context)
	return HttpResponse(pdf,content_type='application/pdf')

