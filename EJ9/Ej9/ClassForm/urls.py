from django.urls import path
from ClassForm import views

urlpatterns=[
	path('',views.formulario,name='formulario'),
	path('Respuesta/',views.formulario,name='respuesta')
]