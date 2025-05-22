from django.contrib import admin
from .models import Articulo

class ArtAdmin(admin.ModelAdmin):
	list_display=("titulo","body")
	prepopulated_fields={"slug":("titulo",)}

admin.site.register(Articulo, ArtAdmin)


	
		
