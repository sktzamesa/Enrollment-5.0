# Generated by Django 5.0.9 on 2024-11-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Enrollments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="Prefered_program",
            field=models.CharField(
                choices=[
                    ("BC", "BS Computer Science"),
                    ("BT", "BS Information Technology"),
                ],
                default="BC",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="admission",
            name="Senior_high_school_strand",
            field=models.CharField(
                choices=[
                    ("ST", "Science, Technology, Engineering and Mathematics"),
                    ("it", "Information Technology"),
                ],
                default="it",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="admission",
            name="senior_high_school_track",
            field=models.CharField(
                choices=[
                    ("AC", "Academic"),
                    ("AD", "Arts and Design"),
                    ("SP", "Sports"),
                    ("TL", "Technical Vocational Livelihood"),
                ],
                default="TL",
                max_length=2,
            ),
        ),
    ]