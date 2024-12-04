from django.db import models

class Instructor(models.Model):
    First_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250,blank=True)
    Last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True)

    def __str__(self):
        return self.First_name
# Create your models here.
