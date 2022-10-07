from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from .forms import BlogForm

# Create your views here.

def index(request):
    return render(request, 'blog/post_index.html', {'data': BlogPost.objects.order_by('-pub_date')})

def post(request, blogpost_slug):
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)
    return render(request, 'blog/view_post.html', {'post': selected_post})

@login_required(login_url="blog:login")
def edit_post(request, blogpost_slug):
    selected_post = get_object_or_404(BlogPost, slug=blogpost_slug)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=selected_post)
        if form.is_valid():
            form.save()
        return redirect('blog:post', blogpost_slug=selected_post.slug)
    elif request.method == "GET":
        form = BlogForm(instance=selected_post)
        return render(request, 'blog/edit_post.html', {'post': selected_post, 'form': form})