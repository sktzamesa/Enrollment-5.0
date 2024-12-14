from django.db import models
from django.conf import settings
class Profile(models.Model):
    User_Student_Profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    date_of_birth = models.DateField(blank=True,null=True)
    Student_profile_photo = models.ImageField(
        upload_to = 'user/%Y/%m/%d',
        blank=True
    )
    Full_name = models.CharField(max_length=250)
    First_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250,blank=True)
    Last_name = models.CharField(max_length=250,blank=True)
    StudentID = models.CharField(max_length=250,unique=True)
    def __str__(self):
        return f"Profile username student {self.User_Student_Profile.username}"
# Create your models here.
