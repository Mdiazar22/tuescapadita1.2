from django.shortcuts import render
from .models import ProductCard

# Create your views here.
def home(request):
    productcards = ProductCard.objects.all()
    return render(request, "planes/home.html", {'productcards':productcards})

def reservar(request):
    return render(request, "planes/reservar.html")