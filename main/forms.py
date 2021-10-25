from django import forms
from .models import Content, UserProfile


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = "__all__"

    def validation_title(self):
        print("Validating text")


