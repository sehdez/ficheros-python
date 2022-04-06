from email.policy import default
from msilib.schema import PublishComponent
from tabnanny import verbose
from turtle import title
from django.db import models

#Importamos CharField
from django.db.models.fields import CharField

# Create your models here.
class Articulo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField( default= 'null')
    public = models.BooleanField()
    creat_at = models.DateTimeField(auto_now_add = True)
    uppdate_at = models.DateTimeField(auto_now=True)
    
    class META:
        #db_table =""
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        
    def __str__(self):
        publicado =""
        if self.public:
            publicado = "Publico"
        else:
            publicado ="Privado"

        return f"{self.id}, {self.title}, ({publicado})"

