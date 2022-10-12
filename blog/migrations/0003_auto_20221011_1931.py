# Generated by Django 4.1.1 on 2022-10-11 18:47

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.utils.text import slugify
from django.apps.registry import Apps


def forwards(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
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


def revert(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    if schema_editor.connection.alias != "default":
        return
    posts = apps.get_model("blog", "BlogPost").objects.all()
    for post in posts:
        post.author = (
            f"{post._author.first_name} {post._author.last_name}".strip()
        )
        post._author.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blogpost__author"),
    ]

    operations = [
        migrations.RunPython(forwards, revert),
    ]
