from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    detalles = models.TextField()
    estado = models.TextField(default="Creada")

    def __str__(self):
        return self.titulo
