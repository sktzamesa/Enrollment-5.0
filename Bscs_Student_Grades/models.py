from django.db import models
from bscs_year_courses.models import FirstYearFirstSemesterCourses
from bscs_year_section.models import FirstYearSection
from django.conf import settings
from bscs_student.models import BSCSStudent

class AcademicYear(models.Model):
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
class FirstYearFirstSemesterStudentGrade(models.Model):
    Student = models.ForeignKey(
        BSCSStudent,
        on_delete = models.CASCADE,
        related_name='First_year_student_grade'
    )
    AcademicYear = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='Academic_year'
    )
    Student_Courses = models.ForeignKey(
        FirstYearFirstSemesterCourses,
        on_delete=models.CASCADE,
        related_name='Student_Course_Grade'
    )
    Grades = models.DecimalField(max_digits=5, decimal_places=2)



