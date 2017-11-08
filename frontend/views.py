from django.shortcuts import render


# Create your views here.

def home_escuelas(request):
    return render(request, 'escuelas.html', {})


def home_estudiantes(request):
    return render(request, 'estudiantes.html', {})
