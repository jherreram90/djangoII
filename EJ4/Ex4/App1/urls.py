from django.urls import path
from App1 import views

urlpatterns=[
	path('',views.v1a1,name='app1')
]