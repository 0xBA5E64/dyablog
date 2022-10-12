from django.contrib import admin

# Register your models here.

from blog.models import BlogPost


class AdminBlogPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, AdminBlogPost)
