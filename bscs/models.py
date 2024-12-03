from django.db import models
from django.conf import settings
from django.utils import timezone

class Student(models.Model):
    Student_Account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'Student_account'
    )
    Full_name = models.CharField(max_length=250)
    First_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250,blank=True)
    Last_name = models.CharField(max_length=250,blank=True)
    Student_number =  models.CharField(max_length=20,unique=True)



