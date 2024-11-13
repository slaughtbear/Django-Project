from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('create/', views.create_project, name='create_project'),
    path('<int:id>/', views.project_detail, name='project_detail')
]