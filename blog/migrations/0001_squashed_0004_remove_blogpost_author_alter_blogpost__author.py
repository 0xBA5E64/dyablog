# Generated by Django 4.1.1 on 2022-10-11 21:04

import django.db.models.deletion
from django.apps.registry import Apps
from django.conf import settings
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.utils.text import slugify


def author_string_to_users(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    if schema_editor.connection.alias != "default":
        return
    posts = apps.get_model("blog", "BlogPost")
    users = apps.get_model("auth", "User")
    for post in posts.objects.all():
        post._author = users.objects.get_or_create(
            username=slugify(post.author),
            first_name=post.author.split(" ")[0],
            last_name=" ".join(post.author.split(" ")[1:]),
        )[0]
        post.save()


def revert_author_string_to_users(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    if schema_editor.connection.alias != "default":
        return
    posts = apps.get_model("blog", "BlogPost").objects.all()
    for post in posts:
        post.author = (
            f"{post._author.first_name} {post._author.last_name}".strip()
        )
        post._author.delete()


class Migration(migrations.Migration):

    replaces = [
        ("blog", "0001_initial"),
        ("blog", "0002_blogpost__author"),
        ("blog", "0003_auto_20221011_1931"),
        ("blog", "0004_remove_blogpost_author_alter_blogpost__author"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=80, verbose_name="Blogpost Title"
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        max_length=40, verbose_name="Blogpost Author"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=240,
                        verbose_name="Blogpost Description",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(verbose_name="Publication Date"),
                ),
                ("body", models.TextField(verbose_name="Blogpost body")),
                (
                    "slug",
                    models.SlugField(
                        unique=True, verbose_name="Blogpost Slug"
                    ),
                ),
                (
                    "_author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RunPython(
            code=author_string_to_users,
            reverse_code=revert_author_string_to_users,
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="author",
        ),
        migrations.RenameField(
            model_name="blogpost",
            old_name="_author",
            new_name="author",
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
