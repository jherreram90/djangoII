from django.urls import path
from catalogo import views

urlpatterns=[
	path('',views.index,name='index'),
	path('lista/',views.PelisListView.as_view(),name='pelis'),
	path('pelicula/<int:pk>',views.PelisDetailView.as_view(),name='pelicula-detalle'),
]