from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ("new","yangi"),
    ("in_process","jarayonda"),
    ("done","Bajarildi"),
    ("canceled","Bekor qilindi"),
]

class Todo(models.Model):
    name = models.CharField('Ish  nomi',max_length=255)
    description = models.TextField('Tavsif')
    status = models.CharField('Holati',choices=STATUS_CHOICES,max_length=10)
