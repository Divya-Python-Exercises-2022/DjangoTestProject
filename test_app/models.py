from django.db import models

# Create your models here.
#from django.db.models import CharField


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)