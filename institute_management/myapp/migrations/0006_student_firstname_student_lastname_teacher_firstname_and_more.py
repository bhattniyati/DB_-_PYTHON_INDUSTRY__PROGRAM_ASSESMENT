# Generated by Django 5.0.1 on 2024-04-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_remove_student_mobile_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="firstname",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="lastname",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacher",
            name="firstname",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="teacher",
            name="lastname",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]