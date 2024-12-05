from django.db import models
from django.conf import settings
from bscs.models import Student

class FirstYearSection(models.Model):
    class FirstYearSectionChoices(models.TextChoices):
        BSCS_1_1 = 'BSCS 1-1', 'BSCS 1-1'
        BSCS_1_2 = 'BSCS 1-2', 'BSCS 1-2'
        BSCS_1_3 = 'BSCS 1-3', 'BSCS 1-3'
        BSCS_1_4 = 'BSCS 1-4', 'BSCS 1-4'
        BSCS_1_5 = 'BSCS 1-5', 'BSCS 1-5'

    first_year_section = models.CharField(
        max_length=8,
        choices=FirstYearSectionChoices,
        default=FirstYearSectionChoices.BSCS_1_1
    )
    class Meta:
        ordering = ['first_year_section']
    def __str__(self):
        return self.first_year_section
class SecondYearSection(models.Model):
    class SecondYearSectionChoices(models.TextChoices):
        BSCS_2_1 = 'BSCS 2-1', 'BSCS 2-1'
        BSCS_2_2 = 'BSCS 2-2', 'BSCS 2-2'
        BSCS_2_3 = 'BSCS 2-3', 'BSCS 2-3'
        BSCS_2_4 = 'BSCS 2-4', 'BSCS 2-4'
        BSCS_2_5 = 'BSCS 2-5', 'BSCS 2-5'

    second_year_section = models.CharField(
        max_length=8,
        choices=SecondYearSectionChoices.choices,
        default=SecondYearSectionChoices.BSCS_2_1
    )


class ThirdYearSection(models.Model):
    class ThirdYearSectionChoices(models.TextChoices):
        BSCS_2_1 = 'BSCS 3-1', 'BSCS 3-1'
        BSCS_2_2 = 'BSCS 3-2', 'BSCS 3-2'
        BSCS_2_3 = 'BSCS 3-3', 'BSCS 3-3'
        BSCS_2_4 = 'BSCS 3-4', 'BSCS 3-4'
        BSCS_2_5 = 'BSCS 3-5', 'BSCS 3-5'

    ThirdYearSection = models.CharField(
        max_length=8,
        choices=ThirdYearSectionChoices,
        default=ThirdYearSectionChoices.BSCS_2_1
    )



class FourthYearSection(models.Model):
    class FourthYearSectionChoices(models.TextChoices):
        BSCS_2_1 = 'BSCS 4-1', 'BSCS 4-1'
        BSCS_2_2 = 'BSCS 4-2', 'BSCS 4-2'
        BSCS_2_3 = 'BSCS 4-3', 'BSCS 4-3'
        BSCS_2_4 = 'BSCS 4-4', 'BSCS 4-4'
        BSCS_2_5 = 'BSCS 4-5', 'BSCS 4-5'

    FourthYearSection = models.CharField(
        max_length=8,
        choices=FourthYearSectionChoices,
        default=FourthYearSectionChoices.BSCS_2_1
    )

# Create your models here.
