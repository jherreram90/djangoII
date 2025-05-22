from django.db import models

class Fun(models.Model):
	Nom=models.CharField(max_length=20)
	Des=models.TextField()
