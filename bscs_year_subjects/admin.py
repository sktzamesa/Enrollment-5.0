from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearFirstSemesterSubject
# Register your models here.
@admin.register(FirstYearFirstSemesterSubject)
class First_Year_Subject(ModelAdmin):
    list_display = ['Subject_code','Subject_name']