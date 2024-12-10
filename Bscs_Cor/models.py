from django.db import models
from bscs_year_subjects.models import FirstYearSubject
from django.conf import settings
# Create your models here.
class Student_COR(models.Model):
    Student = models.ForeignKey(
        settings.AUTH_USER_MODELS,
        on_delete= models.CASCADE,
        related_name='Student_Cor'
    )
    units = models.IntegerField()
    date = models.DateTimeField(timezone.now)
    encoder = models.CharField(max_length=250)
    School_Year = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    time = models.DateTimeField(null=True, blank=True)
    day = models.DateTimeField(null=True, blank=True)
    room = models.CharField(max_length=25)
    shed_Code = models.CharField(default='TBA')
    Course_Description = models.ForeignKey(
        FirstYearSubject,
        related_name='Student Course Description First Year'
    )


