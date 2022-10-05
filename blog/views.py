from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/post_index.html', {'data': BlogPost.objects.order_by('-pub_date'), 'user': request.user})

def post(request, blogpost_slug):
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)
    return render(request, 'blog/view_post.html', {'post': selected_post})

def edit_post(request, blogpost_slug):
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)

    if request.method == "POST":
        selected_post.title = request.POST['title']
        selected_post.author = request.POST['author']
        selected_post.description = request.POST['description']
        selected_post.body = request.POST['body']
        selected_post.save()
        return redirect('blog:post', blogpost_slug=selected_post.slug)
    elif request.method == "GET":
        return render(request, 'blog/edit_post.html', {'post': selected_post})