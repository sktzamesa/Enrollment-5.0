from django.db import models
from bscs_year_subjects.models import FirstYearSubject
# Create your models here.
class FirstYearStudentGrade(models.Model):
    Student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='First_year_student_grade'
    )
    Student_grades = models.ForeignKey(
        FirstYearSubject,
        on_delete=models.CASCADE,
        related_name='Student_grades'
    )
