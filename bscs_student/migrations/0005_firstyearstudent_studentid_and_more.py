# Generated by Django 5.0.9 on 2024-12-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_student", "0004_remove_firstyearstudent_first_year_subject_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="firstyearstudent",
            name="StudentID",
            field=models.CharField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="firstyearstudent",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="StudentProfile/"),
        ),
    ]