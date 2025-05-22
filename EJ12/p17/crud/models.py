from django.db import models

class ListaR(models.Model):
	nombre=models.CharField(max_length=50)
	artista=models.CharField(max_length=100)
	album=models.CharField(max_length=50)
	duracion=models.CharField(max_length=30)

	class Meta:
		db_table='ListaR'
			
	#def_str_(self):
	#	return self.name
		
