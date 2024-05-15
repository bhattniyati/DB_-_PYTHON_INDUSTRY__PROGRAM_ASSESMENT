# Generated by Django 5.0.1 on 2024-05-10 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_student_picture"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="user",
            new_name="userid",
        ),
        migrations.RenameField(
            model_name="teacher",
            old_name="user",
            new_name="userid",
        ),
        migrations.RemoveField(
            model_name="user",
            name="firstname",
        ),
        migrations.RemoveField(
            model_name="user",
            name="lastname",
        ),
        migrations.RemoveField(
            model_name="user",
            name="mobile",
        ),
        migrations.RemoveField(
            model_name="user",
            name="picture",
        ),
        migrations.AddField(
            model_name="teacher",
            name="picture",
            field=models.ImageField(default="", upload_to="T_picture"),
        ),
        migrations.CreateModel(
            name="Principle",
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
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("mobile", models.BigIntegerField()),
                ("picture", models.ImageField(default="", upload_to="P_Picture")),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
    ]