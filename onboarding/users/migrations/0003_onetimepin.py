# Generated by Django 4.2.3 on 2023-08-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_myuser_date_joined_myuser_is_active_myuser_is_staff"),
    ]

    operations = [
        migrations.CreateModel(
            name="OneTimePin",
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
                ("identifier", models.CharField(max_length=255, unique=True)),
                (
                    "identifier_type",
                    models.CharField(
                        choices=[
                            ("EMAIL", "Email"),
                            ("PHONE_NUMBER", "Phone number"),
                        ],
                        max_length=255,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("valid", models.BooleanField(default=True)),
                (
                    "code",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
