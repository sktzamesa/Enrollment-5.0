from django.db import models
from bscs_instructors.models import Instructor
from bscs_year_section.models import FirstYearSection,SecondYearSection,ThirdYearSection,FourthYearSection
# Create your models here.

class FirstYearSubject(models.Model):
    Instructors = models.ForeignKey(
        Instructor,
        on_delete= models.CASCADE,
        related_name='First_year_Instructors'
    )
    FirstYearSubject = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='First_year_Subjects'
    )
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code

class SecondYearSubject(models.Model):
    Instructors = models.ForeignKey(
        Instructor,
        on_delete= models.CASCADE,
        related_name='Second_year_Instructors'
    )
    Second_Year_Subject  = models.ForeignKey(
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

class ThirdYearSubject(models.Model):
    Instructors = models.ForeignKey(
        Instructor,
        on_delete= models.CASCADE,
        related_name='Third_year_Instructors'
    )
    Third_Year_Subject = models.ForeignKey(
        FirstYearSection,
        on_delete=models.CASCADE,
        related_name='Third_Year_Subject'
    )

    Subject_grade = models.CharField(max_length=250)
    Subject_name = models.CharField(max_length=250)
    Subject_code = models.CharField(max_length=250)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.Subject_code

class FourthYearSubject(models.Model):
    Instructors = models.ForeignKey(
        Instructor,
        on_delete= models.CASCADE,
        related_name='Fourth_year_Instructors'
    )
    Fourth_Year_Subject = models.ForeignKey(
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