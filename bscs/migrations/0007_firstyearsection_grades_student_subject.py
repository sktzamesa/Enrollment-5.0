# Generated by Django 5.0.9 on 2024-12-01 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs", "0006_remove_subject_year_section_subject_year_section"),
    ]

    operations = [
        migrations.AddField(
            model_name="firstyearsection",
            name="grades",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="first_year_grade",
                to="bscs.subject",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="subject",
            field=models.ManyToManyField(
                related_name="student_subjects", to="bscs.subject"
            ),
        ),
    ]