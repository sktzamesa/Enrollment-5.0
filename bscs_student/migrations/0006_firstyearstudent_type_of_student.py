# Generated by Django 5.0.9 on 2024-12-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_student", "0005_firstyearstudent_studentid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="firstyearstudent",
            name="Type_of_student",
            field=models.CharField(
                choices=[("RG", "REGULAR"), ("IR", "IRREGULAR")],
                default=1,
                max_length=2,
            ),
            preserve_default=False,
        ),
    ]
