# Generated by Django 5.0.9 on 2024-12-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_year_subjects", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="first_year_subject",
            old_name="Instructor",
            new_name="Instructors",
        ),
        migrations.RenameField(
            model_name="fourth_year_subject",
            old_name="Instructor",
            new_name="Instructors",
        ),
        migrations.RenameField(
            model_name="second_year_subject",
            old_name="Instructor",
            new_name="Instructors",
        ),
        migrations.RenameField(
            model_name="third_year_subject",
            old_name="Instructor",
            new_name="Instructors",
        ),
        migrations.AddField(
            model_name="first_year_subject",
            name="Subject_grade",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="first_year_subject",
            name="Subject_name",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]