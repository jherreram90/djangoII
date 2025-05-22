from django.shortcuts import render
from ClassForm import forms

def formulario(request):
	if request.method=='POST':
		form=forms.Formulario(request.POST)

		if form.is_valid():
			context={
			'nombre':form.cleaned_data['nombre'],
			'email':form.cleaned_data['email'],
			'password':form.cleaned_data['password']
			}
			return render(request,'respuesta.html',context)

	else:
		form=forms.Formulario()

	return render(request,'index2.html',{'form':form})
