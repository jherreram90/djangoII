from django.shortcuts import render
from json import dumps

def antonimo(request):
	data=[
		['Triste','Feliz'], 
		['Frío','Caliente'],
		['Alto','Bajo'],
		['Gordo','Delgado'],
	]
	data=dumps(data)#Crea un json 
	return render(request,'index.html',{'data':data})
