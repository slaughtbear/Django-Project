from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project

@login_required
def create_project(request): # Vista para crear un proyecto
    if request.method == 'GET': # Si el método de acceso a la ruta es GET:
        return render(request, 'pages/create_project.html', { # 1. Se renderiza la página para crear proyectos
            'form': ProjectForm # 2. Con el formulario basado en el modelo 
        })
    else: # Si el método de acceso a la ruta es POST:
        try: # 1. Se usa un bloque de prueba para crear crear un proyecto
            form = ProjectForm(request.POST) # 2. Se crea una instancia del formulario con los datos enviados por el usuario
            new_project = form.save(commit=False) # 3. Se crea el proyecto temporalmente
            new_project.user = request.user # 4. Se asocia el proyecto al usuario que lo creo
            new_project = form.save() # 5. Se almacena el proyecto en la base de datos
            return redirect('projects') # 6. Se redirecciona a la página de proyectos del usuario
        except ValueError: # Si ocurre un error en la creación del proyecto:
            return render(request, 'pages/create_project.html', { # 1. Se renderiza la página para crear proyectos
                'form': ProjectForm, # 2. Con el formulario basado en el modelo 
                'error': 'Por favor introduce correctamente los datos.' # 3. Mandando un mensaje de error
            })

@login_required
def projects(request): # Vista para visualizar todos los proyectos de cada usuario
    # 1. Se crea una instancia del proyecto filtrando proyectos del usuario sin terminar 
    projects = Project.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'pages/projects.html', { # 2. Se renderiza la página de proyectos
        'projects': projects # 3. Con los proyectos en progreso del usuario
    })
