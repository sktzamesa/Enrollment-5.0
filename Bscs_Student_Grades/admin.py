from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearStudentGrade
# Register your models here.
@admin.register(FirstYearStudentGrade)
class FirstYearSectionAdmin(ModelAdmin):
    list_display = ['Student','First_Year_Sections','Student_Subject']