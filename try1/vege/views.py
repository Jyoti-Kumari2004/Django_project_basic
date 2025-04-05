from django.shortcuts import redirect, render
from vege.models import Recepie
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def recepie(request):
    if request.method == "POST":
        data = request.POST
        recepie_name = data.get("recepie_name")
        recepie_description = data.get("recepie_description")
        recepie_image = request.FILES.get("recepie_image")

        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image,
        )
        return redirect("/recepie")
    queryset = Recepie.objects.all()

    if request.GET.get("search"):
        print(request.GET.get("search"))
        queryset = queryset.filter(recepie_name__icontains=request.GET.get("search"))

    context = {"recepies": queryset}

    return render(request, "recepie.html",context)  


@login_required(login_url="/login/")
def delete_recepie(request, id):
    queryset=Recepie.objects.get(id=id)
    queryset.delete()
    return redirect("/recepie/")


@login_required(login_url="/login/")
def update_recepie(request,id):
    queryset=Recepie.objects.get(id=id)
    if request.method=="POST":

        recepie_name = request.POST.get("recepie_name")
        recepie_description =request.POST.get("recepie_description")
        recepie_image = request.FILES.get("recepie_image")

        queryset.recepie_name=recepie_name
        queryset.recepie_description=recepie_description

        if recepie_image:
            queryset.recepie_image=recepie_image
        queryset.save()
        return redirect("/recepie/")
    context={"recepie":queryset}
    return render(request,"update_recepie.html",context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "invalid username")
            return redirect("/login/")
        user = authenticate(username=username, password=password)
        # print(user) # i just checked whats wrong in this code (to debug code)
        if user is None:
            messages.error(request, "Invalid  Password")
            return redirect("/login/")
        else:
            login(
                request, user
            )  # this created a session for that person and saves data for that perosn or id
            return redirect("/recepie/")
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "Account Already exists!!!")
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created sucessfully :) ")
    return render(request, "register.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")
