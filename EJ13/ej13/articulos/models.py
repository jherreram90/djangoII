from django.db import models
from django.urls import reverse 

class Articulo(models.Model):
	titulo=models.CharField(max_length=255)
	body=models.TextField()
	slug=models.SlugField(null=False,unique=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse("detalle",kwargs={"slug":self.slug})


