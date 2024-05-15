# Generated by Django 5.0.1 on 2024-05-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_student_mobile_teacher_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="principle",
            name="picture",
            field=models.ImageField(
                default="default.jpg ", upload_to="media/P_Picture"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="picture",
            field=models.ImageField(default="default.jpg", upload_to="P_Picture"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="picture",
            field=models.ImageField(default="default.jpg", upload_to="P_Picture"),
        ),
    ]