# Generated by Django 4.1.1 on 2022-09-30 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Blogpost Title')),
                ('author', models.CharField(max_length=40, verbose_name='Blogpost Author')),
                ('description', models.CharField(blank=True, max_length=240, verbose_name='Blogpost Description')),
                ('pub_date', models.DateTimeField(verbose_name='Publication Date')),
                ('body', models.TextField(verbose_name='Blogpost body')),
                ('slug', models.SlugField(unique=True, verbose_name='Blogpost Slug')),
            ],
        ),
    ]
