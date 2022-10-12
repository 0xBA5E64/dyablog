from django import forms
from blog.models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'description', 'pub_date', 'body']
        exclude = ['slug', 'author']
