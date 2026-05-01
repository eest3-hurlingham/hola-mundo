from django.shortcuts import render

# PASO 1: una vista simple sin datos
def inicio(request):
    return render(request, 'saludo/inicio.html')

# PASO 2: una vista que recibe datos de la URL y los pasa al template
def saludo(request, nombre):
    contexto = {
        'nombre': nombre,
        'mensaje': '¡Bienvenido a Django!',
    }
    return render(request, 'saludo/saludo.html', contexto)
