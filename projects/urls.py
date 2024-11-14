from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('create/', views.create_project, name='create_project'),
    path('<int:id>/', views.project_detail, name='project_detail'),
    path('<int:id>/complete', views.complete_project, name='complete_project'),
    path('completed/', views.projects_completed, name='projects_completed'),
    path('<int:id>/delete', views.delete_project, name='delete_project')
]