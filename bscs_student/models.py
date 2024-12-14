from django.db import models
from bscs_year_section.models import FirstYearSection,SecondYearSection,ThirdYearSection,FourthYearSection
from bscs_year_courses.models import FirstYearFirstSemesterCourses,FirstYearSecondSemesterCourse,SecondYearFirstSemesterCourses,SecondYearSecondSemesterCourses,ThirdYearFirstSemesterCourses,ThirdYearSecondSemesterCourses,FourthYearFirstSemesterCourses,FourthYearSecondSemesterCourses
from django.conf import settings
from account.models import Profile
# Create your models here.
class BSCSStudent(models.Model):
    class RegularorIrregular(models.TextChoices):
        REGULAR = 'REGULAR','REGULAR'
        IRREGULAR = 'IRREGULAR','IRREGULAR'

    Student = models.ForeignKey(
        Profile,
        on_delete = models.CASCADE,
        related_name = 'Profile_Student'
    )
    Type_of_student = models.CharField(
        max_length=9,
        choices = RegularorIrregular
    )
    First_year_section = models.ForeignKey(
        FirstYearSection,
        on_delete = models.CASCADE,
        related_name = 'fist_year_section_student',
        blank = True,
        null=True
    )
    first_year_first_semester_courses = models.ManyToManyField(
        FirstYearFirstSemesterCourses,
        related_name='FirstYearFirstSemesterStudentsCourses',
        blank=True
    )
    First_Year_Second_Semester_Course = models.ManyToManyField(
        FirstYearSecondSemesterCourse,
        related_name='FirstYearFirstSemesterStudentsCourses',
        blank=True
    )
    SecondYearSection = models.ForeignKey(
        SecondYearSection,
        on_delete = models.CASCADE,
        related_name = 'second_year_section_student',
        blank=True,
        null=True

    )
    Second_Year_First_Semester_Courses = models.ManyToManyField(
        SecondYearFirstSemesterCourses,
        related_name='SecondYearFirstSemesterStudentCourses',
        blank=True
    )
    Second_Year_Second_Semester_Courses = models.ManyToManyField(
        SecondYearSecondSemesterCourses,
        related_name='SecondYearSecondSemesterStudentCourses',
        blank=True
    )
    ThirdYearSection = models.ForeignKey(
        ThirdYearSection,
        on_delete = models.CASCADE,
        related_name = 'Third_year_section_student',
        blank=True,
        null=True
    )
    ThirdYearFirstSemesterCourses = models.ManyToManyField(
        ThirdYearFirstSemesterCourses,
        related_name='ThirdYearFirstSemesterStudentCourses',
        blank=True
    )
    ThirdYearSecondSemesterCourses = models.ManyToManyField(
        ThirdYearSecondSemesterCourses,
        related_name='ThirdYearSecondThirdSemesterCourses',
        blank=True
    )
    FourthYearSection = models.ForeignKey(
        FourthYearSection,
        on_delete = models.CASCADE,
        related_name = 'Fourth_year_section_student',
        blank=True,
        null=True
    )
    FourthYearFirstSemesterCourses = models.ManyToManyField(
        FourthYearFirstSemesterCourses,
        related_name='FourthYearFirstSemesterStudentCourses',
        blank=True
    )
    FourthYearSecondSemesterCourses = models.ManyToManyField(
        FourthYearSecondSemesterCourses,
        related_name='FourthYearSecondSemesterStudentCourses',
        blank=True
    )