# Generated by Django 5.0.9 on 2024-12-01 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bscs", "0004_remove_secondyearsection_created_at_and_more"),
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
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Student_first_year",
                to="bscs.student",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fourthyearsection",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Student_Fourth_year",
                to="bscs.student",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="secondyearsection",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Student_Second_year",
                to="bscs.student",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="thirdyearsection",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Third_first_year",
                to="bscs.student",
            ),
            preserve_default=False,
        ),
    ]
