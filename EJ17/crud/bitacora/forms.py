from django.forms import ModelForm
from .models import Tarea

class CreateTaskForm(ModelForm):
	class Meta:
		model=Tarea
		fields=['titulo','desc','urgente']

