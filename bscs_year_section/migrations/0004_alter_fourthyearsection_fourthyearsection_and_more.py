# Generated by Django 5.0.9 on 2024-12-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_year_section", "0003_remove_firstyearsection_room_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fourthyearsection",
            name="FourthYearSection",
            field=models.CharField(
                choices=[
                    ("BSCS 4-1", "BSCS 2-1"),
                    ("BSCS 4-2", "BSCS 2-2"),
                    ("BSCS 4-3", "BSCS 2-3"),
                    ("BSCS 4-4", "BSCS 2-4"),
                    ("BSCS 4-5", "BSCS 2-5"),
                ],
                default="BSCS 4-1",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="thirdyearsection",
            name="ThirdYearSection",
            field=models.CharField(
                choices=[
                    ("BSCS 3-1", "BSCS 2-1"),
                    ("BSCS 3-2", "BSCS 2-2"),
                    ("BSCS 3-3", "BSCS 2-3"),
                    ("BSCS 3-4", "BSCS 2-4"),
                    ("BSCS 3-5", "BSCS 2-5"),
                ],
                default="BSCS 3-1",
                max_length=8,
            ),
        ),
    ]
