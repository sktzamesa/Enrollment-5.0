# Generated by Django 5.0.9 on 2024-12-02 11:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bscs_student", "0001_initial"),
        ("bscs_year_section", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="First_year_Student",
            new_name="FirstYearStudent",
        ),
    ]
