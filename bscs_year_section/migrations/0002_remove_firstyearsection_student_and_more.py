# Generated by Django 5.0.9 on 2024-12-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_year_section", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="firstyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="fourthyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="secondyearsection",
            name="student",
        ),
        migrations.RemoveField(
            model_name="thirdyearsection",
            name="student",
        ),
        migrations.AddField(
            model_name="firstyearsection",
            name="room_number",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
