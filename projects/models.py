from django.db import models
from django.contrib.auth.models import User  # Modelo de usarios de Django

class Project(models.Model):
    # Constantes
    FRONTEND = 'FE'
    BACKEND = 'BE'
    FULLSTACK = 'FS'
    OTHER = 'O'
    AREA_CHOICES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (FULLSTACK, 'Fullstack'),
        (OTHER, 'Otro'),
    ]
    # Propiedades del modelo
    name = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=2, choices=AREA_CHOICES)
    done = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        status = "Completado" if self.done else "En progreso"
        return f'{self.name} - {self.get_area_display()} ({status})'
