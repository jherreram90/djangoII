from django.shortcuts import render
import numpy as np

def chart(request):
	labels=['Mexico','EUA','Noruega']
	data=[200,300,295]
	context={
		'labels':labels,
		'data':data
	}
	return render(request,'index.html',context)

def chart2(request):
	x=np.linspace(-5,5,10000)#Arreglo numpy 
	y=-1*(x**3)+2*x**2+x#Arreglo numpy, esta define una VD.
	context={
		'labels':x,
		'data':y,
	}
	return render(request,'index2.html',context)

def chart3(request):
	return render(request,'index3.html',{})




















