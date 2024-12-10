from django.db import models
from bscs_year_section.models import FirstYearSection
from bscs_year_subjects.models import FirstYearFirstSemesterSubject
from django.conf import settings

# Create your models here.
class FirstYearFirstSemesterStudent(models.Model):
    class RegularorIrregular(models.TextChoices):
        REGULAR = 'RG','REGULAR'
        IRREGULAR = 'IR','IRREGULAR'
    Full_name = models.CharField(max_length=250)
    First_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250,blank=True)
    Last_name = models.CharField(max_length=250,blank=True)
    profile_picture = models.ImageField(upload_to='StudentProfile/', blank=True)
    StudentID = models.CharField(max_length=250,unique=True)
    Student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='Students',
    )
    Type_of_student = models.CharField(
        max_length=2,
        choices = RegularorIrregular
    )
    year_section = models.ForeignKey(
        FirstYearSection,
        on_delete = models.CASCADE,
        related_name = 'year_section_student'
    )
    first_year_subject = models.ManyToManyField(
        FirstYearFirstSemesterSubject,
        related_name='FirstYearStudents'
    )