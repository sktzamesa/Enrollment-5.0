# Generated by Django 5.0.9 on 2024-11-24 05:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Enrollments", "0011_admission_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="Father_Contact_number",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Father_Occupation",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Father_has_attended_college",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Fathers_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Guardian_Contact_number",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Guardian_Occupation",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Guardian_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Mother_Contact_number",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Mother_Occupation",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Mother_has_attended_college",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="admission",
            name="Mother_name",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]