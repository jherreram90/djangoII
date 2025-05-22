from django.db import models
from django.contrib.auth.models import User

class Actividad(models.Model):
	titulo=models.CharField(max_length=100)
	desc=models.TextField(blank=True)
	creado=models.DateTimeField(auto_now_add=True)
	completado=models.DateTimeField(null=True)
	urgente=models.BooleanField(default=False)
	user=models.ForeignKey(User, on_delete=models.CASCADE) #la crea un usuario, relación sql.
	
	def __str__(self):
		return self.titulo+'-by '+self.user.username



