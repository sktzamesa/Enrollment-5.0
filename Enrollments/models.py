from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.conf import settings

class Admission(models.Model):
    class Applicant(models.TextChoices):
        Senior_High_School_Graduate = 'SH','Senior HighSchool Graduate'
        Alternative_Learning_System = 'AL', 'Alternative Learning System'
        Currently_enrolled_Grade12_student= 'CE','Currently enrolled Grade12 student'
        Bachelor_degree_graduate = 'BD','Bachelor degree graduate'
        Teacher_certificate_program_applicant = 'TC','Teacher certificate program applicant'
        Transferee = 'TF','Transferee'
        Diploma_certificate_associate_vocationalgraduate = 'DC','Diploma certificate associate vocational graduate'
    
    class SHSTrack(models.TextChoices):
        academic = 'AC','Academic'
        arts_and_design = 'AD','Arts and Design'
        sports = 'SP','Sports'
        TVL = 'TL','Technical Vocational Livelihood'

    class SHSStrand(models.TextChoices):
        stem = 'ST','Science, Technology, Engineering and Mathematics'
        ict = 'it','Information Technology'

    class PreferredProgram(models.TextChoices):
        BSCS = 'BC','BS Computer Science'
        BSIT = 'BT','BS Information Technology'

    class IncomeBracket(models.TextChoices):
        LOW = '0', '0-25k'
        MEDIUM = '1', '25k-50k'
        HIGH = '2', '50k-100k'
        VERY_HIGH = '3', '100k+'
    class Waitlist(models.TextChoices):
        PENDING = 'PE', 'PENDING'
        DONE = 'DO', 'DONE'


    Type_of_applicant = models.CharField(
        max_length= 2,
        choices=Applicant,
    )
    senior_high_school_track = models.CharField(
        max_length= 2,
        choices = SHSTrack,
    )
    Senior_high_school_strand = models.CharField(
        max_length= 2,
        choices=SHSStrand,
    )
    Preferred_program = models.CharField(
        max_length= 2,
        choices = PreferredProgram,
    )
    Waitlist = models.CharField(
        max_length=2,
        choices=Waitlist,
        default = Waitlist.PENDING
    )

    full_name = models.CharField(max_length=250)
    Given_name = models.CharField(max_length=250)
    Middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    Suffix = models.CharField(max_length=250, blank=True)
    Date_of_birth = models.DateField()
    Contact_number = models.CharField(max_length=250)
    photo = models.ImageField(
        upload_to='user/%Y/%m/%d',
        blank=True
    )
    Address_line_1= models.CharField(max_length=250)
    Address_line_2= models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    State_Province_Region = models.CharField(max_length=250)
    Postal_code = models.CharField(max_length=250)
    number_of_siblings = models.IntegerField(default=0)
    income_bracket = models.CharField(
        max_length=1,
        choices=IncomeBracket.choices,
        default=IncomeBracket.LOW
    )
    Fathers_name = models.CharField(max_length=250,blank=True)
    Father_Contact_number = models.CharField(max_length=250,blank=True)
    Father_Occupation = models.CharField(max_length=250,blank=True)
    Father_has_attended_college = models.BooleanField()
    Mother_name = models.CharField(max_length=250,blank=True)
    Mother_Contact_number = models.CharField(max_length=250,blank=True)
    Mother_Occupation = models.CharField(max_length=250,blank=True)
    Mother_has_attended_college = models.BooleanField()
    Guardian_name = models.CharField(max_length=250)
    Guardian_Contact_number = models.CharField(max_length=250)
    Guardian_Occupation = models.CharField(max_length=250)
    Elementary_School_name = models.CharField(max_length=250)
    Elementary_School_Address = models.CharField(max_length=250)
    Elementary_Type_of_school = models.CharField(max_length=250)
    Elementary_Year_of_graduated = models.CharField(max_length=250)
    Senior_High_School_Name = models.CharField(max_length=250)
    Senior_High_School_Address = models.CharField(max_length=250)
    Senior_High_School_Type_of_School = models.CharField(max_length=250)
    Senior_High_School_Graduated = models.CharField(max_length=250)
    College_School_name = models.CharField(max_length=250)
    College_Enrolled_Program = models.CharField(max_length=250)
    College_School_Address = models.CharField(max_length=250)
    College_Type_of_School = models.CharField(max_length=250)
    College_Year_Graduated = models.CharField(max_length=250)
    Report_Card = models.ImageField(
        upload_to='Admission/Report_Card/%Y/%m/%d',
    )
    Form_137 = models.ImageField(
        upload_to='Admission/Form137/%Y/%m/%d',
    )
    Passport = models.ImageField(
        upload_to= 'Admission/passport/%Y/%m/%d',
        blank=True
    )
    Additional_Documents = models.ImageField(
        upload_to='Admission/passport/%Y/%m/%d',
        blank=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    publish_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-create_at']

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return f"{settings.MEDIA_URL}{self.photo}"
        return None

    def __str__(self):
        return self.full_name














