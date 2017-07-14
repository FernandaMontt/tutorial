from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	Curso = models.CharField(max_length=200)
	Sigla = models.CharField(max_length=10)
	Categoria = models.TextField(max_length=100)
	horario_creacion = models.DateTimeField(
	default = timezone.now)
	horario_publicacion = models.DateTimeField(
	blank=True, null=True)
	
def publicacion(self):
	self.horario_publicacion = timezone.now()
	self.save()

def __str__(self):
	return self.title
	
