from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Categoria, Marca
from .forms import ProductoForm

# Create your views here.
def inicio(request):
    return render(request, "paginas/index.html")

#Tabla productos, muestra todos los productos
def productos(request):
    productos = Producto.objects.all()
    return render(request, "crud/mostrar.html", {'productos': productos})

def contacto(request):
    return render(request, "paginas/contacto.html")

def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, "crud/insertar.html", {'formulario': formulario})

def editar(request):
    return render(request, "crud/editar.html")

def eliminar(request, id):
    producto = Producto.objects.get(producto_id=id)
    producto.delete()
    return redirect('productos')

