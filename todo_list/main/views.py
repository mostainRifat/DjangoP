from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "index.html")


def alltasks(request):
    getalltasks = Tasksmodel.objects.exclude(isCompleted="True").all()
    return render(request, "alltasks.html", {"alltasksins": getalltasks})


def completedtasks(request):
    donetasks = Tasksmodel.objects.filter(isCompleted="True").all()
    return render(request, "completedtasks.html", {"alltasksins": donetasks})


def add(request):
    return render(request, "add.html")


def addbackend(request):
    if request.method == "POST":
        t = request.POST["title"]
        d = request.POST.get("description")
        c = request.POST.get("isCompleted") == "on"
        task = Tasksmodel(title=t, description=d, isCompleted=c)
        task.save()

    return HttpResponseRedirect(
        reverse("alltasks")
    ) 


def delete(request, task_id):
    task = Tasksmodel.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("alltasks"))


def deletecompleted(request, task_id):
    task = Tasksmodel.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("completedtasks"))


def edit(request, task_id):
    ins = Tasksmodel.objects.get(id=task_id)
    return render(request, "rewrite.html", {"ct": ins})


def editbackend(request, task_id):
    if request.method == "POST":
        ins = Tasksmodel.objects.get(id=task_id)  # old one
        t = request.POST["title"]
        d = request.POST.get("description")
        c = request.POST.get("isCompleted") == "on"
        ins.title = t
        ins.description = d
        ins.isCompleted = c
        ins.save()
    return HttpResponseRedirect(reverse("alltasks"))


def editbackendforcompleted(request, task_id):
    if request.method == "POST":
        ins = Tasksmodel.objects.get(id=task_id)  # old one
        t = request.POST["title"]
        d = request.POST.get("description")
        c = request.POST.get("isCompleted") == "on"
        ins.title = t
        ins.description = d
        ins.isCompleted = True
        ins.save()
    return HttpResponseRedirect(reverse("completedtasks"))


def complete(request, task_id):
    task = Tasksmodel.objects.get(id=task_id)
    task.isCompleted = True
    task.save()  # important
    return HttpResponseRedirect(reverse("completedtasks"))


def incomplete(request, task_id):
    task = Tasksmodel.objects.get(id=task_id)
    task.isCompleted = False
    task.save()  # important
    return HttpResponseRedirect(reverse("alltasks"))
