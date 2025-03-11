from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>heyyy yaa all</h1>")

def sucess(request):
    return HttpResponse("i am sucess page dear")
def trail(request):
    return render(request,'index.html')