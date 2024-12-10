from django.db import models
from bscs_year_section.models import FirstYearSection,SecondYearSection,ThirdYearSection,FourthYearSection
# Create your models here.

class FirstYearFirstSemesterSubject(models.Model):
    FirstYearSections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='First_Year_First_Semester_Subject'
    )
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code
class FirstYearSecondSemesterSubject(models.Model):
    FirstYearSections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='First_YearSecond_Semester_Subject'
    )
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code

class SecondYearFirstSemesterSubject(models.Model):
    Second_Year_Sections  = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Second_year_Subjects'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)
    def __str__(self):
        return self.Subject_code

class SecondYearSecondSemesterSubject(models.Model):
    Second_Year_Sections  = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Second_Year_Second_Semester_Subject'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)
    def __str__(self):
        return self.Subject_code

class ThirdYearFirstSemesterSubject(models.Model):
    Third_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Third_Year_First_Semester_Subject'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code
class ThirdYearSecondSemesterSubject(models.Model):
    Third_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Third_Year_Second_Semester_Subject'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code
class FourthYearFirstSemesterSubject(models.Model):
    Fourth_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Fourth_year_subjects'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code

class FourthYearSecondSemesterSubject(models.Model):
    Fourth_Year_Sections = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Fourth_Year_Second_Semester_Subject'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code