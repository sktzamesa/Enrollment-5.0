from django.db import models
from bscs_year_subjects.models import FirstYearFirstSemesterSubject
from bscs_year_section.models import FirstYearSection
from django.conf import settings

class FirstYearStudentGrade(models.Model):
    Student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='First_year_student_grade'
    )
    Student_Subject = models.ForeignKey(
        FirstYearFirstSemesterSubject,
        on_delete=models.CASCADE,
        related_name='Student_grades'
    )
    Grades = models.DecimalField(max_digits=5, decimal_places=2)
    First_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name = 'First_year_Sections'
    )

