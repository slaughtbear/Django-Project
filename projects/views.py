from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, 'pages/create_project.html', {
            'form': ProjectForm
        })
    else:
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project = form.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'pages/create_project.html', {
                'form': ProjectForm,
                'error': 'Por favor introduce correctamente los datos.'
            })

@login_required
def projects(request):
    return render(request, 'pages/projects.html')
