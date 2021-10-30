from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Content, UserProfile
from django.http import HttpResponse
from .forms import ContentForm
from django.contrib import messages


def index_page(request):
    qs = Content.objects.all()
    context = {
        "posts": qs
    }
    return render(request, "main/index.html", context)


def content_creation(request):
    form = ContentForm()
    if request.method == "POST":
        form = ContentForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return HttpResponse("<h1>Congrats</h1>")

        messages.error(request, "Invalid data provided")
        print("Invalid data")

    context = {
        "form": form,
    }

    return render(request, "main/content_create.html", context)


def content_update(request, pk):
    obj = Content.objects.get(pk=pk)
    form = ContentForm(instance=obj)

    if request.method == "POST":
        form = ContentForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            print("Saved")
            return HttpResponse("<h1>Congrats</h1>")

        messages.error(request, "Invalid data provided")
        print("Invalid data")

    context = {
        "form": form,
    }
    return render(request, "main/content_create.html", context)


def content_delete(request):

    context = {

    }

    return render(request, "main/content_delete.html", context)



def content_detail(request):

    context = {
        
    }

    return render(request, "main/content_detail.html", context)

