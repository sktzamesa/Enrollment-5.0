from django.db import models
from bscs_year_courses.models import FirstYearFirstSemesterCourses
class FirstYearFirstSemesterInstructor(models.Model):
    First_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250,blank=True)
    Last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True)
    FirstYearFirstSemesterCourse = models.ForeignKey(
        FirstYearFirstSemesterCourses,
        on_delete= models.CASCADE,
        related_name='FirstYearCoursesInstructor'
    )

    def __str__(self):
        return self.First_name
# Create your models here.
