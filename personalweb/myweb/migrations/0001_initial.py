# Generated by Django 4.2.14 on 2024-09-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomepageContent",
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
                ("title", models.CharField(max_length=200)),
                ("subtitle", models.CharField(max_length=300)),
                ("body", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
