from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Content, UserProfile
from django.http import HttpResponse


def index_page(request):
    qs = User.objects.all()
    context = {
        "users": qs
    }
    return render(request, "main/index.html", context)

