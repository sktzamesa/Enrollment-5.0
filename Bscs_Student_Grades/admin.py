from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearFirstSemesterStudentGrade,AcademicYear
# Register your models here.
@admin.register(FirstYearFirstSemesterStudentGrade)
class FirstYearSectionAdmin(ModelAdmin):
    list_display = ['Student']

@admin.register(AcademicYear)
class AcademicYearAdmin(ModelAdmin):
    list_display = ['start_year','end_year']