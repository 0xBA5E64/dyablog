from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.index, name='index'),
  path('login/',
    auth_views.LoginView.as_view(
      template_name='blog/login.html',
      next_page="blog:index"
      ),
    name='login'
  ),
  path('<slug:blogpost_slug>/', views.post, name='post')
]