from django.contrib import admin
from django.urls import path
from bitacora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
