from django.urls import path
from plantilla import views

urlpatterns=[
	path('',views.Alumno1,name='Alumno1'),
	path('2/',views.Alumno2,name='Alumno2'),
]