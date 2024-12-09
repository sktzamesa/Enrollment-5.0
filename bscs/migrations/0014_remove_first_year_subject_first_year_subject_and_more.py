# Generated by Django 5.0.9 on 2024-12-02 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bscs", "0013_student_student_account"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="first_year_subject",
            name="First_Year_Subject",
        ),
        migrations.RemoveField(
            model_name="first_year_subject",
            name="Instructor",
        ),
        migrations.RemoveField(
            model_name="firstyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="fourth_year_subject",
            name="Fourth_Year_Subject",
        ),
        migrations.RemoveField(
            model_name="second_year_subject",
            name="Second_Year_Subject",
        ),
        migrations.RemoveField(
            model_name="third_year_subject",
            name="Third_Year_Subject",
        ),
        migrations.RemoveField(
            model_name="fourth_year_subject",
            name="Instructor",
        ),
        migrations.RemoveField(
            model_name="fourthyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="second_year_subject",
            name="Instructor",
        ),
        migrations.RemoveField(
            model_name="secondyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="third_year_subject",
            name="Instructor",
        ),
        migrations.RemoveField(
            model_name="thirdyearsection",
            name="student",
        ),
        migrations.DeleteModel(
            name="First_year_Student",
        ),
        migrations.DeleteModel(
            name="First_Year_Subject",
        ),
        migrations.DeleteModel(
            name="FirstYearSection",
        ),
        migrations.DeleteModel(
            name="Fourth_Year_Subject",
        ),
        migrations.DeleteModel(
            name="FourthYearSection",
        ),
        migrations.DeleteModel(
            name="Second_Year_Subject",
        ),
        migrations.DeleteModel(
            name="SecondYearSection",
        ),
        migrations.DeleteModel(
            name="Third_Year_Subject",
        ),
        migrations.DeleteModel(
            name="ThirdYearSection",
        ),
    ]
