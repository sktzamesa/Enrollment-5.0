from django.db import models
from bscs_year_courses.models import FirstYearFirstSemesterCourses
from bscs_year_section.models import FirstYearSection
from django.conf import settings

class FirstYearFirstSemesterStudentGrade(models.Model):
    Student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='First_year_student_grade'
    )
    Student_Courses = models.ForeignKey(
        FirstYearFirstSemesterCourses,
        on_delete=models.CASCADE,
        related_name='Student_Course_Grade'
    )
    Grades = models.DecimalField(max_digits=5, decimal_places=2)


