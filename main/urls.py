from django.urls import path
from main import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index_page"),
    path("content_create/", views.ContentCreationView.as_view(), name="content_create"),
    path("content_update/<int:pk>/", views.ContentUpdateView.as_view(), name="content_update"),
    path("details/<int:id>/", views.ContentDetailView.as_view(), name="content_detail"),
    path("delete/<int:number>/", views.content_delete, name="content_delete"),

    # path("user/login/", views.login_user),
    path("user/login/", LoginView.as_view(template_name="user/login.html"), ),
    path("user/phone/login/", views.login_with_phone),
    path("user/logout/", views.logout_user, ),
    path("user/register/", views.register_user, ),

    path("send_mail", views.send_mail_to_someone)

]
