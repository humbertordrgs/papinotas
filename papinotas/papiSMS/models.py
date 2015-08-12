from django.db import models

# Create your models here.

class Colegio(models.Model):
    nombre = models.CharField(max_length=200)
		
    

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    colegio = models.ForeignKey(Colegio)
    colegio.db_column='colegio'
		    

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso)
    curso.db_column='curso'

