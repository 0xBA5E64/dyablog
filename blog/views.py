from select import select
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/post_index.html', {'data': BlogPost.objects.all()})

def post(request, blogpost_id):
    selected_post = get_object_or_404(BlogPost, id=blogpost_id)
    return render(request, 'blog/view_post.html', {'data': selected_post})