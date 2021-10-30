from django.urls import path
from main import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("content_create/", views.content_creation, name="content_create"),
    path("content_update/<int:pk>/", views.content_update, name="content_update"),
    path("detail/", views.content_detail),
    path("delete/", views.content_delete),

]
