from django.contrib import admin
from .models import Actividad

class ActividadAdmin(admin.ModelAdmin):
	readonly_fields=('creado',)
		
admin.site.register(Actividad,ActividadAdmin)
