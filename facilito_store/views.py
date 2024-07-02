from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from products.models import Product
from .forms import RegisterForm


def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message':'Listado de productos',
        'title': 'Productos',
        'products': products,    
    })


def logi_view(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect('login')

# Obtener información de un formulario basado en una clase. 
def register(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, "Usuario creado exitosamente")
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })