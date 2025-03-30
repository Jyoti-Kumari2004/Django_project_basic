from django.shortcuts import redirect, render
from todo.models import TodoItem


# Create your views here.
def home_todo(request):
    if request.method == "POST":
        data = request.POST
        task_domain = data.get("task_domain")
        task_description = data.get("task_description")
        task_due_date = data.get("task_due_date")

        TodoItem.objects.create(
            task_domain=task_domain,
            task_description=task_description,
            task_due_date=task_due_date,
        )
        return redirect("/todo")
    queryset = TodoItem.objects.all()
    context = {"todos": queryset}

    return render(request, "home_todo.html", context)

def delete_todo(request,id):
    queryset=TodoItem.objects.get(id=id)
    queryset.delete()
    return redirect('/table_todo/')

def update_todo(request,id):
    queryset=TodoItem.objects.get(id=id)
    if request.method=="POST":
        task_domain = request.POST.get("task_domain")
        task_description = request.POST.get("task_description")
        task_due_date = request.POST.get("task_due_date")
        queryset.task_domain=task_domain
        queryset.task_description=task_description
        queryset.task_due_date=task_due_date
        queryset.save()
        return redirect("/table_todo/")
    context={"todos":queryset}
    return render(request,"update_todo.html",context)


def table_todo(request):
    queryset = TodoItem.objects.all()
    context = {"todos": queryset}
    return render(request,"table_todo.html",context)

