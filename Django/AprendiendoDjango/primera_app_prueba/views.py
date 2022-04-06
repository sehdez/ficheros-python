from turtle import title
from django.shortcuts import render,HttpResponse, redirect
from miapp.views import articulo
from primera_app_prueba.models import Articulo
from django.db.models import Q
from primera_app_prueba.forms import FormArticulo
from django.contrib import messages

# Create your views here.

def index1 (request):
    return render(request, 'index1.html')



def articles (request):





    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form= formulario.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Articulo(
                title = title,
                content = content,
                public = public
            )
            articulo.save()
            

            # Mensaje flash
            messages.success(request,f'Has Creado correctamente el artículo: {articulo.title}')
            return redirect ('articles')
    else:
        formulario = FormArticulo()
        articulos = Articulo.objects.all().order_by('title')
    return render(request, 'articles.html',{
        'form':formulario,
        'articulos':articulos
    })

def articles1(request):
    articulos = Articulo.objects.all().order_by('title')
    return render(request, 'articles1.html',{
        'articulos':articulos
    })






def delete(request, id):
    articulo= Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('articles')


