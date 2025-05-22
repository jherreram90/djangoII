from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
	class Meta:
		model=Task
		fields=['title','description','important']
		widgets={
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe titulo'}),
			'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Añade descripción'}),
			#'important':forms.CheckboxInput(attrs={'class':'form-check-input text-center'}),
			'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
		}

