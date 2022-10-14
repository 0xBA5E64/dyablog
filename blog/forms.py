from django import forms
from blog.models import BlogPost
from typing import Any


class BlogForm(forms.ModelForm[Any]):
    class Meta:
        model = BlogPost
        fields = ["title", "author", "description", "pub_date", "body"]
        exclude = ["slug", "author"]
