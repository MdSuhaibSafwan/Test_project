from django import forms
from .models import Content, UserProfile

# Validation check --> 1. Object level validation, 2. Full validation


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        # fields = "__all__"
        exclude = ["user", ]

    def clean_text(self):
        print("Validating text inside forms")
        text = self.cleaned_data.get("text")
        print(text)

        if "django" not in text:
            raise forms.ValidationError("Blog is not about Django")

        return text

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # user = self.cleaned_data.get("user")  # it is none
        user = self.instance.user  # Since we made it in view as form.instance.user = request.user
        print("User ", user.username)
        print("Title ", title)

        qs = Content.objects.filter(user=user, title=title)
        if qs.exists():
            raise forms.ValidationError("User has already created a blog of this title")

        return title
