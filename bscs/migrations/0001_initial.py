# Generated by Django 5.0.9 on 2024-12-01 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FirstYearSection",
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
                    "first_year_section",
                    models.CharField(
                        choices=[
                            ("BSCS 1-1", "BSCS 1-1"),
                            ("BSCS 1-2", "BSCS 1-2"),
                            ("BSCS 1-3", "BSCS 1-3"),
                            ("BSCS 1-4", "BSCS 1-4"),
                            ("BSCS 1-5", "BSCS 1-5"),
                        ],
                        default="BSCS 1-1",
                        max_length=8,
                    ),
                ),
            ],
            options={
                "ordering": ["first_year_section"],
            },
        ),
        migrations.CreateModel(
            name="SecondYearSection",
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
                    "second_year_section",
                    models.CharField(
                        choices=[
                            ("BSCS 2-1", "BSCS 2-1"),
                            ("BSCS 2-2", "BSCS 2-2"),
                            ("BSCS 2-3", "BSCS 2-3"),
                            ("BSCS 2-4", "BSCS 2-4"),
                            ("BSCS 2-5", "BSCS 2-5"),
                        ],
                        default="BSCS 2-1",
                        max_length=8,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
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
                ("name", models.CharField(max_length=250)),
                (
                    "User_Instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Instructors",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "year_section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="year_sections",
                        to="bscs.firstyearsection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("Full_name", models.CharField(max_length=250)),
                ("First_name", models.CharField(max_length=250)),
                ("Middle_name", models.CharField(blank=True, max_length=250)),
                ("Last_name", models.CharField(blank=True, max_length=250)),
                (
                    "Student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Students",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "year_section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="year_section_student",
                        to="bscs.firstyearsection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("Subject_code", models.CharField(max_length=250)),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instructor_subjects",
                        to="bscs.instructor",
                    ),
                ),
                (
                    "year_section",
                    models.ManyToManyField(
                        related_name="Subjects", to="bscs.firstyearsection"
                    ),
                ),
            ],
        ),
    ]
