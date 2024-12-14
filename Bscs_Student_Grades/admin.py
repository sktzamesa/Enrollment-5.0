from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearFirstSemesterStudentGrade
# Register your models here.
@admin.register(FirstYearFirstSemesterStudentGrade)
class FirstYearSectionAdmin(ModelAdmin):
    list_display = ['Student']