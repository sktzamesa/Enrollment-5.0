from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    date_of_birth = models.DateField(blank=True,null=True)
    profile_photo = models.ImageField(
        upload_to = 'user/%Y/%m/%d',
        blank=True
    )
    def __str__(self):
        return f"Profile username student of {self.user.username}"
# Create your models here.
