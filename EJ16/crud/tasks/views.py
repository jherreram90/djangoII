from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import CreateTaskForm
from .forms import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'home.html')

def CreateUsr(request):
	if request.method=='GET':
		return render(request, 'signup.html',{'form':UserCreationForm})
	else:
		#registrar usuario
		if request.POST['password1']==request.POST['password2']:
			try:
				user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request, user) #Guarda las cookies para gestion de info usr
				return redirect('tasks') #redirecciona
			except IntegrityError: #Excepción, verifica si el usr ya está creado
				return render(request, 'signup.html',
					{'form':UserCreationForm, 
					'error':'El usuario ya existe'})
		return render(request, 'signup.html',
			{'form':UserCreationForm,
			'error':'Las contraseñas no coinciden'})

@login_required
def tasks(request):
	tareas=Task.objects.filter(user=request.user,datecompleted__isnull=True)#filtra para mostrar tareas que no se han completado de usuario logueado
	return render(request,'tasks.html',{'tareas':tareas})

@login_required
def task_detail(request,task_id):
	if request.method=='GET':
		tarea=get_object_or_404(Task,pk=task_id,user=request.user)#permite ver/actualizar sólo tareas del usr logueado
		form=CreateTaskForm(instance=tarea)
		return render(request,'tasks_detail.html',{'form':form,'tarea':tarea})
	else:
		try:
			tarea=get_object_or_404(Task,pk=task_id,user=request.user)#permite actualizar sólo tareas del usr logueado
			form=CreateTaskForm(request.POST, instance=tarea)
			form.save()
			return redirect('tasks')
		except ValueError:
			return render(request,'tasks_detail.html',{'form':form, 'tarea':tarea, error:'error'})

@login_required
def complete_task(request,task_id):
	tarea=get_object_or_404(Task,pk=task_id,user=request.user)
	if request.method=='POST':
		tarea.datecompleted=timezone.now()
		tarea.save()
		return redirect('tasks')

@login_required
def task_completed(request):
	tareas=Task.objects.filter(user=request.user,
	datecompleted__isnull=False).order_by('-datecompleted')#filtra para mostrar tareas que no se han completado de usuario logueado
	return render(request,'tasks.html',{'tareas':tareas})

@login_required
def delete_task(request,task_id):
	tarea=get_object_or_404(Task, pk=task_id,  user=request.user)
	if request.method=='POST':
		tarea.delete()
		return redirect('tasks')

@login_required
def Create_task(request):
	if request.method=='GET':
		return render(request,'create_task.html', {'form':CreateTaskForm})
	else:
		try:
			form=CreateTaskForm(request.POST)
			new_task=form.save(commit=False)
			new_task.user=request.user
			new_task.save()
			return redirect('tasks')
		except ValueError:
			return render(request,'create_task.html', 
				{'form':CreateTaskForm,
				'error':'ingresa datos validos'})

@login_required #se redirecciona con linea 107 de settings
def signout(request):
	logout(request)
	return redirect('home')

def signin(request):
	if request.method=='GET': #Si se capturan datos
		return render(request, 'signin.html', {'form':AuthenticationForm})
	else: #Si se envían datos
		user=authenticate(request, 
			username=request.POST['username'], 
			password=request.POST['password'])
		if user is None:
			return render(request, 'signin.html', 
			{'form':AuthenticationForm, 
			'error':'Usuario o password incorrecto'})
		else:	
			login(request,user)
			return redirect('tasks')


	