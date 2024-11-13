from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from django.utils import timezone

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
    # 1. Se crea una instancia del proyecto filtrando proyectos del usuario que no se han completado 
    projects = Project.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'pages/projects.html', { # 2. Se renderiza la página de proyectos
        'projects': projects # 3. Con los proyectos en progreso del usuario
    })

@login_required
def project_detail(request, id): # Vista para ver detalles de un proyecto y actualizarlo
    if request.method == 'GET': # Si el método de acceso a la ruta es GET:
        # 1. Se crea una instancia del proyecto filtando por el id y el usuario
        project = get_object_or_404(Project, pk=id, user=request.user) # Si el proyecto no existe se obtiene un error 404
        # 2. Se crea una instancia del formulario para crear un proyecto
        form = ProjectForm(instance=project) # Con los datos del proyecto que se solicita por id
        return render(request, 'pages/project_detail.html', { # 3. Se renderiza la página la información del proyecto
            'project': project, # 4. Con todos los datos del proyecto
            'form': form # 5. Y el formulario para actualizar esos datos
        })
    else: # Si el método de acceso a la ruta es POST:
        try:  # 1. Se usa un bloque de prueba para crear crear un proyecto
            # 2. Se crea una instancia del proyecto filtando por el id y el usuario
            project = get_object_or_404(Project, pk=id, user=request.user)
            # 3. Se crea una instancia del formulario con los datos enviados por el usuario
            form = ProjectForm(request.POST, instance=project) 
            form.save() # 4. Se almacenan los cambios en la base de datos
            return redirect('projects') # 5. Se redirecciona a la página de proyectos del usuario
        except ValueError: # Si ocurre un error en la actualización del proyecto:
            return render(request, 'pages/project_detail.html', { # 1. Se renderiza la página la información del proyecto
            'project': project, # 2. Con todos los datos del proyecto
            'form': form, # 5. Con el formulario para actualizar esos datos
            'error': 'Error actualizando tarea...' # 6. Mandando un error al usuario
        })

@login_required
def complete_project(request, id): # Vista para marcar un proyecto como completado
    project = get_object_or_404(Project, pk=id, user=request.user) # Se crea una instancia del proyecto filtando por el id y el usuario
    if request.method == 'POST': # Si el método de acceso a la ruta es POST:
        project.date_completed = timezone.now() # 1. Se actualiza la fecha de completado
        project.save() # 2. Se almacenan los cambios en la base de datos
        return redirect('projects') # 3. Se redirecciona a la página de proyectos del usuario