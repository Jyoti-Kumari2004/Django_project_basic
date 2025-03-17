from django.shortcuts import redirect, render
from vege.models import Recepie


# Create your views here.
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
    context = {"recepies": queryset}
        
    return render(request, "recepie.html",context)  

def delete_recepie(request, id):
    queryset=Recepie.objects.get(id=id)
    queryset.delete()
    return redirect("/recepie/")
    
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