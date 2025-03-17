from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "core/home.html")


def sucess(request):
    return render(request, "core/sucess.html")

def trail(request):
    peoples = [
        {"name": "example", "age": 45},
        {"name": "Jyoti", "age": 25},
        {"name": "Pranshu", "age": 27},
        {"name": "Navin", "age": 42},
        {"name": "Neelam", "age": 40},
    ]

    return render(request, "core/index.html", context={"peoples": peoples})
