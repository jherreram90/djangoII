from django.shortcuts import render, redirect, get_object_or_404 #Primero render, luego redirect, luego get object
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #primero crear luego authtentication
from django.contrib.auth.forms import User #se ocupa para registrar usuario
from django.db import IntegrityError#se usa para registrar_usuario
from django.contrib.auth import login, logout, authenticate #primero logout
#from .forms import CreateTaskForm
#from .forms import Actividad
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'home.html')

def registrar_usuario(request):
	if request.method=='GET':
		return render(request, 'registrar_usuario.html',
			{'form':UserCreationForm})
	else:
		#registrar usuario
		if request.POST['password1']==request.POST['password2']:
			try:
				user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request, user) #Guarda las cookies para gestion de info usr
				return redirect('registrar_usuario') #redirecciona
			except IntegrityError: #Excepción, verifica si el usr ya está creado
				return render(request, 'registrar_usuario.html',
					{'form':UserCreationForm, 
					'error':'El usuario ya existe'})
		return render(request, 'registrar_usuario.html',
			{'form':UserCreationForm,
			'error':'Las contraseñas no coinciden'})