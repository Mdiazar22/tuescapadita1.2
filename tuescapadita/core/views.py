from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "core/login.html")

def registro(request):
    return render(request, "core/registro.html")