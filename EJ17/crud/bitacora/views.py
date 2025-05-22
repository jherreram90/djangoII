from django.shortcuts import render, redirect, get_object_or_404 #Primero render, luego redirect, luego get object
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #primero crear luego authtentication
from django.contrib.auth.forms import User #se ocupa para registrar usuario
from django.db import IntegrityError#se usa para registrar_usuario
from django.contrib.auth import login, logout, authenticate #primero logout
from .forms import CreateTaskForm
from .forms import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'home.html')

#meter modelo a admin.py
#Registrar superusuario
def registrar_usuario(request):
	if request.method=='GET':
		return render(request, 'registrarse.html',{'form':UserCreationForm})
	else:
		#registrar usuario
		if request.POST['password1']==request.POST['password2']:
			try:
				user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request, user) #Guarda las cookies para gestion de info usr
				return redirect('registrar_usuario') #redirecciona
			except IntegrityError: #Excepción, verifica si el usr ya está creado
				return render(request, 'registrarse.html',
					{'form':UserCreationForm, 
					'error':'El usuario ya existe'})
		return render(request, 'registrarse.html',
			{'form':UserCreationForm,
			'error':'Las contraseñas no coinciden'})

@login_required
def cerrar_sesion(request):
	logout(request)
	return redirect('home')

def iniciar_sesion(request):
	if request.method=='GET': #Si se capturan datos
		return render(request, 'inicia_sesion.html', {'form':AuthenticationForm})
	else: #Si se envían datos
		user=authenticate(request, 
			username=request.POST['username'], 
			password=request.POST['password'])
		if user is None:
			return render(request, 'inicia_sesion.html', 
			{'form':AuthenticationForm, 
			'error':'Usuario o password incorrecto'})
		else:	
			login(request,user)
			return redirect('tareas')

@login_required
def tareas(request):
	tareas=Tarea.objects.filter(user=request.user,completado__isnull=True)#filtra para mostrar tareas que no se han completado de usuario logueado
	return render(request,'tareas.html',{'tareas':tareas})

@login_required
def agregatarea(request):
	if request.method=='GET':
		return render(request,'crear_tarea.html', {'form':CreateTaskForm})
	else:
		try:
			form=CreateTaskForm(request.POST)
			new_task=form.save(commit=False)
			new_task.user=request.user
			new_task.save()
			return render(request,'detalle_tareas.html',{'form':form, 'tarea':tarea, error:'error'})

@login_required
def completartarea(request,task_id):
	tarea=get_object_or_404(Tarea,pk=task_id,user=request.user)
	if request.method=='POST':
		tarea.completado=timezone.now()
		tarea.save()
		return redirect('tareas')

@login_required
def tareacompletada(request):
	tareas=Tarea.objects.filter(user=request.user,
	completado__isnull=False).order_by('-completado')#filtra para mostrar tareas que no se han completado de usuario logueado
	return render(request,'tareas.html',{'tareas':tareas})

@login_required
def eliminartarea(request,task_id):
	tarea=get_object_or_404(Tarea, pk=task_id,  user=request.user)
	if request.method=='POST':
		tarea.delete()
		return redirect('tareas')
