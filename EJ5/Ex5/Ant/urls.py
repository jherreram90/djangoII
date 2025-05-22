from django.urls import path
from Ant import views

urlpatterns=[
	path('',views.antonimo,name='index')
]