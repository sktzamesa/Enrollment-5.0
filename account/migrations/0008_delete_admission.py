# Generated by Django 5.0.9 on 2024-11-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0007_remove_admission_date_of_birth_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Admission",
        ),
    ]
