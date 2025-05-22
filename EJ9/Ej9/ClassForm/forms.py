from django import forms

class Formulario(forms.Form):
	nombre=forms.CharField(label='Nombre', max_length=50, 
		help_text='Acá va el nombre',
		widget=forms.TextInput(
			attrs={'placeholder':'Escribe tu nombre',
			'style':'border-color:red;',})
		)
	email=forms.EmailField(label='Email', max_length=50,
		help_text='Acá va el mail',
		widget=forms.TextInput(
			attrs={'placeholder':'Acá va el mail',
			'style':'border-color:blue;',})
		)
	password=forms.CharField(label='Password',
		widget=forms.PasswordInput(), 
		help_text='Campo requerido')
 
    