# Generated by Django 5.0.1 on 2024-04-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
