# Generated by Django 5.0.9 on 2024-12-06 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "bscs_year_section",
            "0005_alter_fourthyearsection_fourthyearsection_and_more",
        ),
        (
            "bscs_year_subjects",
            "0006_rename_firstyearsubject_firstyearsubject_firstyearsections_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FirstYearStudentGrade",
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
                ("Grades", models.DecimalField(decimal_places=2, max_digits=5)),
                ("date_recorded", models.DateTimeField(auto_now_add=True)),
                (
                    "First_Year_Sections",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="First_year_Sections",
                        to="bscs_year_section.firstyearsection",
                    ),
                ),
                (
                    "Student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="First_year_student_grade",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "Student_Subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Student_grades",
                        to="bscs_year_subjects.firstyearsubject",
                    ),
                ),
            ],
        ),
    ]