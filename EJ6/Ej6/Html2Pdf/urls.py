from django.urls import path
from Html2Pdf import views

urlpatterns=[
	path('',views.index,name='index'),
	path('1/',views.GenPdf,name='GenPdf'),
]