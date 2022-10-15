# Generated by Django 4.1.1 on 2022-10-11 20:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_auto_20221011_1931"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="author",
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RenameField(
            model_name="blogpost", old_name="_author", new_name="author"
        ),
    ]
