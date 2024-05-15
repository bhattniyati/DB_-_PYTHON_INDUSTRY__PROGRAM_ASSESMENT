# Generated by Django 5.0.1 on 2024-04-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254)),
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("mobile", models.PositiveBigIntegerField()),
                ("password", models.CharField(max_length=20)),
                ("picture", models.ImageField(default="", upload_to="Profile_Picture")),
            ],
        ),
    ]
