from django.urls import path
from main import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
]
