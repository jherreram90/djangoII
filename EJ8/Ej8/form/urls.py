from django.urls import path
from form import views

urlpatterns=[
	path('',views.index,name='index'),
	path('mostrar/',views.index),
]
