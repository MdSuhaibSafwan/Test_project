from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Content, UserProfile
from django.http import HttpResponse
from .forms import ContentForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    qs = Content.objects.all().order_by("-last_updated")
    context = {
        "posts": qs
    }
    return render(request, "main/index.html", context)


def content_creation(request):
    form = ContentForm()
    if request.method == "POST":
        form = ContentForm(data=request.POST)
        if form.is_valid():
            obj = form.save()
            print("Saved")
            return redirect("content_detail", id=obj.id)

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
            return HttpResponse("<h1>Congrats</h1>")  # task to redirect to detail

        messages.error(request, "Invalid data provided")
        print("Invalid data")

    context = {
        "form": form,
    }
    return render(request, "main/content_create.html", context)


def content_delete(request, number):
    try:
        obj = Content.objects.get(id=number)
    except ObjectDoesNotExist:
        return HttpResponse(f"Content with this Id ({number}) is not found To delete")

    if request.method == "POST":
        obj.delete()
        # messages.success(request, "Content has been deleted")
        return redirect("index_page")

    context = {
        "post_obj": obj
    }

    return render(request, "main/content_delete.html", context)



def content_detail(request, id):
    try:
        obj = Content.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(f"Content with this Id ({id}) is not found")

    context = {
        "post_obj": obj
    }

    return render(request, "main/content_detail.html", context)

