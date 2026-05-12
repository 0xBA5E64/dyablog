from django import forms

from blog.models import BlogPost, CommentPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "description", "body"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ["body"]
        exclude = ["author", "timestamp", "parent_post"]
