from django.contrib import admin
from .models import Content, Tag, ContentImage, UserVerificationOTp, UserProfile

class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "text")


admin.site.register(UserProfile)
admin.site.register(Content, ContentAdmin)
admin.site.register(Tag)
admin.site.register(ContentImage)
admin.site.register(UserVerificationOTp)
