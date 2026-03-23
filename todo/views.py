from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")

        if title:  # validation (no empty tasks)
            Task.objects.create(title=title)

        return redirect('index')
    
    return render(request, 'todo/index.html', {'tasks': tasks})

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed  # toggle
    task.save()
    return redirect('index')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('index')