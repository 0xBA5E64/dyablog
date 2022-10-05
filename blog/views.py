import imp
from select import select
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/post_index.html', {'data': BlogPost.objects.order_by('-pub_date'), 'user': request.user})

def post(request, blogpost_slug):
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)
    return render(request, 'blog/view_post.html', {'post': selected_post})