from django.urls import path
from App2 import views

urlpatterns=[
	path('',views.v1a2,name='app2')
]