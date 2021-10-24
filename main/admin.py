from django.contrib import admin
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "text")


admin.site.register(Content, ContentAdmin)
