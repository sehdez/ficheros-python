"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importar vistas miapp
from miapp import views as views_miapp
# Importar vistas primera_app_prueba
from primera_app_prueba import views as views_app_prueba


urlpatterns = [
    path('admin/', admin.site.urls),
    # Urls de miapp
    path('', views_app_prueba.index1, name = "index1"),
    path('inicio/', views_miapp.index, name = "inicio"),
    path('hola_mundo/', views_miapp.hola_mundo, name="hola_mundo"),
    path('pagina/', views_miapp.pagina, name="pagina"),
    path('pagina/<int:redirigir>', views_miapp.pagina, name="pagina"),
    # URL con parametros opcionales
    path('contacto/', views_miapp.contacto, name="contacto"),
    path('contacto/<str:nombre>', views_miapp.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', views_miapp.contacto, name="contacto"),
    path('articulo/<str:id>/<str:public>', views_miapp.articulo, name = "articulo"),
    path('editar-articulo/<str:id>', views_miapp.editar_articulo, name = "editar_articulo"),
    path('articulos/', views_miapp.articulos, name = "articulos"),
    path('borrar-articulo/<str:id>', views_miapp.borrar_articulo, name = "borrar_articulo"),
    path('crear-articulo/', views_miapp.crear_articulo, name = "crear_articulo"),
    path('guardar-articulo/', views_miapp.guardar_articulo, name = "guardar_articulo"),
    path('create-article/',views_miapp.create_article, name = "create_article"),
    
    # URLs de primera_app_prueba
    path('index/', views_app_prueba.index1, name = "index1"),
    path('articles/', views_app_prueba.articles, name = "articles"),
    path('articles1/', views_app_prueba.articles1, name = "articles1"),
    path('delete/<str:id>', views_app_prueba.delete, name = "delete"),
   
]
