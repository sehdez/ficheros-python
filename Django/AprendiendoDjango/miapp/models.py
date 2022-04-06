from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default= 'null')
    public = models.BooleanField()
    creat_at = models.DateTimeField(auto_now_add=True)
    uppdated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_at = models.DateTimeField()

