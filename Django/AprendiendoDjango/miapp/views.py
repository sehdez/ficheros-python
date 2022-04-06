from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q 
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.

def index(request):
    lenguas = ["Php", "JavaScript", "Python"]
    year = 2022
    rango = range (year, 2051)


    return render(request, 'index.html', {
        'mi_variable':'5',
        'title':'Inicio', 
        'lenguajes':lenguas,
        'rango': rango
         })


def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('index')

    return render(request, "pagina.html")


def contacto(request, nombre="", apellido = ""):
    html = ""
    if nombre and apellido:
        html += f"<h3>El nombre completo es: {nombre} {apellido}</h3>"

    return render(request,"contacto.html" )

def guardar_articulo(request):
    

    #if request.method=='GET':
    if request.method == 'POST':

        title= request.POST['title']
        content= request.POST['content']
        public= request.POST['public']
        articulo = Article(

            title = title,
            content = content,
            public = public
        )
        articulo.save()

        


        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")



def create_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            articulo.save()

             # crear  mensaje flash (Sólo se muestra una vez)
            messages.success(request, f'Has creado correctamente el artículo: {articulo.title}')

            return redirect('articulos')
            #return HttpResponse (title + ' ' + content + ' ' + str(public))

    else:
        formulario = FormArticle()
    
    return render(request, 'create_article.html',{
        'form': formulario,
    })



    


def crear_articulo(request):
    return render(request,'crear_articulo.html')

def articulo(request, id, public):
    
    try:
        articulo = Article.objects.get(id= id, public = public)
        response = f"Articulo: {articulo.title} {articulo.content}"
    except:
        response= "Articulo no encontrado"
    
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo= Article.objects.get(pk = id)

    articulo.title = "Articulo editado"
    articulo.content = "Descripción del articulo actualizado"
    articulo.public = False
    articulo.save()
    return HttpResponse("El articulo ha sido actualizado")

def articulos(request):
    #articulos = Article.objects.filter(title = "Batman", content__contains="articulo" ,content__iexact="articulo", id__gte=12, id__lt= 12 )
    #articulos = Article.objects.order_by('id')[2:7]
    articulos = Article.objects.all().order_by('title')
    # articulos = Article.objects.raw("Consulta de SQL")
    """
    articulos = Article.objects.filter().exclude(public= True)
    articulos = Article.objects.filter(
        Q(title__contains ="2") | Q(title__contains="3")
    )
    """
    return render (request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
