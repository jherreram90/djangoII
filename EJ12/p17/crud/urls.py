from django.urls import path
from . import views

urlpatterns=[
	path('', views.Listar.as_view(),name='list'),
	path('crear', views.Crear.as_view(), name='crear'),
	path('<int:pk>', views.VistaInd.as_view(), name='detalle'),
	path('<int:pk>/update', views.Actualizar.as_view(), name='actualiza'),
	path('<int:pk>/delete', views.Eliminar.as_view(), name='elimina'),
]