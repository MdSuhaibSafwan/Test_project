from django import forms
from .models import Content, UserProfile

# Validation check --> 1. Object level validation, 2. Full validation


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = "__all__"

    def clean_text(self):
        print("Validating text inside forms")
        text = self.cleaned_data.get("text")
        print(text)

        if "django" not in text:
            raise forms.ValidationError("Blog is not about Django")

        return text

