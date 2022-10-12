from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField("Blogpost Title", max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(
        "Blogpost Description", max_length=240, blank=True
    )
    pub_date = models.DateTimeField("Publication Date")
    body = models.TextField("Blogpost body")
    slug = models.SlugField("Blogpost Slug", null=False, unique=True)

    def __str__(self):
        return self.title
