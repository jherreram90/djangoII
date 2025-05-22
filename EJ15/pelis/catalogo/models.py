from django.db import models
from django.urls import reverse

class Director(models.Model):
	nombre=models.CharField(max_length=100, help_text='nombre de director')
	apellido=models.CharField(max_length=100, help_text='nombre de director')

	def get_absolute_url(self):
		return reverse('author-detail',args=[str(self.id)])
		
	def __str__(self):
		return '%s %s'%(self.nombre,self.apellido)

class Pelicula(models.Model):
	titulo=models.CharField(max_length=50)
	autor=models.ManyToManyField(Director)
	resumen=models.TextField(max_length=100,help_text='Resumen')

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('pelicula-detalle',args=[str(self.id)])



