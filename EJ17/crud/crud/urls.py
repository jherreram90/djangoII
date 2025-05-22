from django.contrib import admin
from django.urls import path
from bitacora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registrar/', views.registrar_usuario,name='registrar_usuario'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/crear/', views.agregatarea, name='agregar_tarea'),
    path('tareas/<int:task_id>/', views.detalletarea, name='detalle_tarea'),
    path('tareas/<int:task_id>/completar', views.completartarea, name='completar_tarea'),
    path('tareas/completada', views.tareacompletada, name='completadas'),
    path('tareas/<int:task_id>/eliminar', views.eliminartarea, name='eliminar_tarea'),
]
