from django.contrib import admin
from .models import Project

# Clase para modificar la interfaz de Projects en el panel de administrador
class ProjectAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', ) # Campos de la base que son de sólo lectura

admin.site.register(Project, ProjectAdmin) # Registro del modelo Task dentro del panel de administrador