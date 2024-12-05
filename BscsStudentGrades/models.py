from django.db import models
from bscs_year_subjects.models import FirstYearSubject
from bscs_year_section import FirstYearSection
from bscs_year_subjects import FirstYearSection
# Create your models here.
class FirstYearStudentGrade(models.Model):
    Student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='First_year_student_grade'
    )
    Student_Subject = models.ForeignKey(
        FirstYearSubject,
        on_delete=models.CASCADE,
        related_name='Student_grades'
    )
    Grades = models.CharField(max_length=20)
    First_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name = 'First_year_Sections'
    )
    date_recorded = models.DateTimeField(auto_now_add=True)
