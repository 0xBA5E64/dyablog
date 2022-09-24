from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField('Blogpost Title', max_length=80)
    author = models.CharField('Blogpost Author', max_length=40)
    description = models.CharField("Blogpost Description", max_length=240, blank=True)
    pub_date = models.DateTimeField('Publication Date')
    body = models.TextField('Blogpost body')

    def __str__(self):
        return self.title