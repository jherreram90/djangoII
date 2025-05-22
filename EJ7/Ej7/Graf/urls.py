from django.urls import path
from Graf import views

urlpatterns=[
	path('',views.chart,name='chart1'),
	path('2/',views.chart2,name='chart2'),
	path('3/',views.chart3,name='chart3'),
]